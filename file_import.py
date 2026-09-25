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


# ---------------------------------------------------------------------------
# Generic tabular loaders (for charting — no lat/lon required)
# ---------------------------------------------------------------------------
_LABEL_VALUE_PATTERN = re.compile(r"^(.+?)[:\-\u2013,]\s*(-?\d[\d,]*\.?\d*)\s*%?\s*$")


def load_csv_generic(uploaded_file) -> pd.DataFrame:
    """Load any CSV as-is (no lat/lon requirement) for charting."""
    try:
        uploaded_file.seek(0)
    except Exception:
        pass
    try:
        raw = pd.read_csv(uploaded_file)
    except Exception as e:
        raise FileImportError(f"Could not read this CSV file: {e}")
    if raw is None or raw.empty:
        raise FileImportError("The CSV file has no rows.")
    raw.columns = [str(c).strip() for c in raw.columns]
    return raw


def _extract_pdf_best_table(uploaded_file):
    tables = _extract_pdf_tables(uploaded_file)
    if not tables:
        return None
    best = max(tables, key=len)
    header, *body = best
    try:
        df = pd.DataFrame(body, columns=header)
        df.columns = [str(c).strip() for c in df.columns]
        return df
    except Exception:
        return None


def _parse_pdf_label_value(text: str) -> pd.DataFrame:
    """Fallback: parse lines like 'Wheat: 25000' or 'Cotton - 8.2%' into a
    two-column Label/Value table, useful for charting simple report figures."""
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        m = _LABEL_VALUE_PATTERN.match(line)
        if not m:
            continue
        label = m.group(1).strip(" -:,\t")
        try:
            value = float(m.group(2).replace(",", ""))
        except ValueError:
            continue
        if not label:
            continue
        rows.append({"Label": label, "Value": value})
    if not rows:
        raise FileImportError(
            "No tables or 'Label: number' style lines were found in this PDF for charting."
        )
    return pd.DataFrame(rows)


def load_pdf_generic(uploaded_file) -> pd.DataFrame:
    """Load a PDF's best table, or fall back to label/value text lines, for charting."""
    try:
        import pdfplumber  # noqa: F401
    except ImportError:
        raise FileImportError(
            "PDF support requires the 'pdfplumber' package. Install it with "
            "`pip install pdfplumber` (see requirements.txt) and restart the app."
        )
    uploaded_file.seek(0)
    try:
        df = _extract_pdf_best_table(uploaded_file)
    except Exception:
        df = None
    if df is not None and not df.empty:
        return df

    uploaded_file.seek(0)
    text = _extract_pdf_text(uploaded_file)
    return _parse_pdf_label_value(text)


def load_any_generic(uploaded_file) -> pd.DataFrame:
    """Load a Streamlit UploadedFile (.csv or .pdf) as a raw table for charting."""
    filename = (getattr(uploaded_file, "name", "") or "").lower()
    if filename.endswith(".csv"):
        return load_csv_generic(uploaded_file)
    if filename.endswith(".pdf"):
        return load_pdf_generic(uploaded_file)
    raise FileImportError("Unsupported file type — please upload a .csv or .pdf file.")
