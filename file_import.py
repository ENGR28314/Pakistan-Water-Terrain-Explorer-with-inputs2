"""
file_import.py
Turns a user-uploaded CSV or PDF file into a standardized DataFrame with
'Name', 'Latitude' and 'Longitude' columns (plus any extra columns kept for
hover text), so it can be handed straight to map_view.custom_points_map().

CSV: any table with recognizable latitude/longitude columns.
PDF: either a table with the same kind of columns, or plain text containing
     coordinate pairs (e.g. "Site A: 31.52, 74.35" or "31.52N, 74.35E").
"""

import re
import pandas as pd

LAT_ALIASES = {"lat", "latitude", "y"}
LON_ALIASES = {"lon", "lng", "long", "longitude", "x"}
NAME_ALIASES = {"name", "label", "place", "location", "site", "title", "point", "city"}
CATEGORY_ALIASES = {"category", "type", "group", "class"}


class FileImportError(Exception):
    """Raised when the uploaded file can't be turned into map points."""


def _match_column(columns, aliases):
    for col in columns:
        if str(col).strip().lower() in aliases:
            return col
    return None


def _standardize(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        raise FileImportError("No rows were found in the uploaded file.")

    df = df.copy()
    df.columns = [str(c).strip() for c in df.columns]

    lat_col = _match_column(df.columns, LAT_ALIASES)
    lon_col = _match_column(df.columns, LON_ALIASES)
    if lat_col is None or lon_col is None:
        raise FileImportError(
            "Couldn't find latitude/longitude columns. Expected headers such as "
            "'lat'/'latitude' and 'lon'/'longitude' (or 'lng', 'x', 'y')."
        )
    name_col = _match_column(df.columns, NAME_ALIASES)
    category_col = _match_column(df.columns, CATEGORY_ALIASES)

    out = pd.DataFrame()
    out["Name"] = (
        df[name_col].astype(str) if name_col else [f"Point {i + 1}" for i in range(len(df))]
    )
    out["Latitude"] = pd.to_numeric(df[lat_col], errors="coerce")
    out["Longitude"] = pd.to_numeric(df[lon_col], errors="coerce")
    if category_col:
        out["Category"] = df[category_col].astype(str)

    used = {lat_col, lon_col, name_col, category_col}
    for c in df.columns:
        if c not in used and c not in out.columns:
            out[c] = df[c]

    out = out.dropna(subset=["Latitude", "Longitude"])
    out = out[out["Latitude"].between(-90, 90) & out["Longitude"].between(-180, 180)]
    if out.empty:
        raise FileImportError(
            "No valid latitude/longitude rows were found after parsing "
            "(values may be missing or out of range)."
        )
    return out.reset_index(drop=True)


# ---------------------------------------------------------------------------
# CSV
# ---------------------------------------------------------------------------
def load_csv(uploaded_file) -> pd.DataFrame:
    try:
        raw = pd.read_csv(uploaded_file)
    except Exception as e:
        raise FileImportError(f"Could not read this CSV file: {e}")
    return _standardize(raw)


# ---------------------------------------------------------------------------
# PDF
# ---------------------------------------------------------------------------
_COORD_PATTERN = re.compile(
    r"(-?\d{1,3}(?:\.\d+)?)\s*°?\s*[NnSs]?\s*[,;]\s*(-?\d{1,3}(?:\.\d+)?)\s*°?\s*[EeWw]?"
)


def _extract_pdf_tables(uploaded_file):
    import pdfplumber

    tables = []
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            for tbl in page.extract_tables():
                if tbl and len(tbl) > 1:
                    tables.append(tbl)
    return tables


def _extract_pdf_text(uploaded_file) -> str:
    import pdfplumber

    uploaded_file.seek(0)
    chunks = []
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            chunks.append(page.extract_text() or "")
    return "\n".join(chunks)


def _parse_pdf_text_coords(text: str) -> pd.DataFrame:
    rows = []
    for i, line in enumerate(text.splitlines()):
        line = line.strip()
        if not line:
            continue
        m = _COORD_PATTERN.search(line)
        if not m:
            continue
        try:
            lat, lon = float(m.group(1)), float(m.group(2))
        except ValueError:
            continue
        if not (-90 <= lat <= 90 and -180 <= lon <= 180):
            continue
        label = line[: m.start()].strip(" -:,\t") or f"Point {i + 1}"
        rows.append({"Name": label, "Latitude": lat, "Longitude": lon})
    if not rows:
        raise FileImportError(
            "No coordinate pairs were found in the PDF. Include a table with "
            "latitude/longitude columns, or lines like 'Site A: 31.52, 74.35'."
        )
    return pd.DataFrame(rows)


def load_pdf(uploaded_file) -> pd.DataFrame:
    try:
        import pdfplumber  # noqa: F401
    except ImportError:
        raise FileImportError(
            "PDF support requires the 'pdfplumber' package. Install it with "
            "`pip install pdfplumber` (see requirements.txt) and restart the app."
        )

    uploaded_file.seek(0)
    try:
        tables = _extract_pdf_tables(uploaded_file)
    except Exception:
        tables = []

    if tables:
        best = max(tables, key=len)
        header, *body = best
        try:
            raw = pd.DataFrame(body, columns=header)
            return _standardize(raw)
        except FileImportError:
            pass  # fall through and try text-based extraction instead
        except Exception:
            pass

    text = _extract_pdf_text(uploaded_file)
    raw = _parse_pdf_text_coords(text)
    return _standardize(raw)


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------
def load_any(uploaded_file) -> pd.DataFrame:
    """Load a Streamlit UploadedFile (.csv or .pdf) into a standardized DataFrame."""
    filename = (getattr(uploaded_file, "name", "") or "").lower()
    if filename.endswith(".csv"):
        return load_csv(uploaded_file)
    if filename.endswith(".pdf"):
        return load_pdf(uploaded_file)
    raise FileImportError("Unsupported file type — please upload a .csv or .pdf file.")
