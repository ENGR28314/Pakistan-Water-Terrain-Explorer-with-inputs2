"""
water_quality_engine.py
Water-quality index engine for river-basin monitoring: electrical
conductivity (EC), pH and dissolved oxygen (DO), classified against
published guideline thresholds (WHO drinking-water guidance, Pakistan's
NSDWQ, and FAO irrigation-water guidelines — see data_loader.SOURCES for
citations). Includes an illustrative synthetic-snapshot generator so the
classification and charting logic can be demonstrated without a live sensor
feed; the same classify_* functions work unchanged on real EC/pH/DO readings.

Run standalone:
    python water_quality_engine.py --seed 3 --out water_quality.png
"""

import argparse

import numpy as np
import pandas as pd

DEFAULT_BASINS = ["Indus", "Jhelum", "Chenab", "Ravi", "Sutlej", "Kabul"]

# Guideline threshold bands compiled from WHO drinking-water guidance,
# Pakistan's National Standards for Drinking Water Quality (NSDWQ), and FAO
# irrigation-water guidelines. See data_loader.SOURCES for citations.
WATER_QUALITY_THRESHOLDS = {
    "EC_uS_cm": {
        "good_max": 1000, "marginal_max": 2700, "unit": "µS/cm",
        "note": "FAO irrigation guidance: <700 no restriction, 700–3000 slight-to-moderate, >3000 severe restriction.",
    },
    "pH": {
        "good_range": (6.5, 8.5), "unit": "pH units",
        "note": "WHO / Pakistan NSDWQ acceptable range for drinking water is 6.5–8.5.",
    },
    "DO_mg_L": {
        "good_min": 6.0, "marginal_min": 4.0, "unit": "mg/L",
        "note": "DO > 6 mg/L: good for aquatic life; 4–6 mg/L: stressed; < 4 mg/L: poor/hypoxic.",
    },
}


def classify_ec(value: float) -> str:
    t = WATER_QUALITY_THRESHOLDS["EC_uS_cm"]
    if value <= t["good_max"]:
        return "Good"
    if value <= t["marginal_max"]:
        return "Marginal"
    return "Poor"


def classify_ph(value: float) -> str:
    lo, hi = WATER_QUALITY_THRESHOLDS["pH"]["good_range"]
    return "Good" if lo <= value <= hi else "Marginal"


def classify_do(value: float) -> str:
    t = WATER_QUALITY_THRESHOLDS["DO_mg_L"]
    if value >= t["good_min"]:
        return "Good"
    if value >= t["marginal_min"]:
        return "Marginal"
    return "Poor"


def generate_synthetic_water_quality(basins=None, seed=None) -> pd.DataFrame:
    """Illustrative single-reading-per-basin water-quality snapshot (EC, pH, DO)."""
    basins = basins or DEFAULT_BASINS
    rng = np.random.default_rng(seed)
    rows = []
    for basin in basins:
        ec = float(rng.uniform(300, 2200))
        ph = float(rng.uniform(6.8, 8.9))
        do = float(rng.uniform(3.0, 9.0))
        rows.append({
            "Basin": basin,
            "EC_uS_cm": round(ec, 1),
            "pH": round(ph, 2),
            "DO_mg_L": round(do, 2),
            "EC_class": classify_ec(ec),
            "pH_class": classify_ph(ph),
            "DO_class": classify_do(do),
        })
    return pd.DataFrame(rows)


def composite_water_quality_index(row) -> float:
    """
    Simple composite score (0-100): 100 = all three parameters 'Good', 0 =
    all 'Poor'. An illustrative equal-weighted aggregate for quick
    comparison across basins — not a validated national WQI formula.
    """
    score_map = {"Good": 100, "Marginal": 55, "Poor": 15}
    scores = [score_map[row["EC_class"]], score_map[row["pH_class"]], score_map[row["DO_class"]]]
    return round(sum(scores) / len(scores), 1)


def plot_water_quality(df: pd.DataFrame, out_path: str = "water_quality.png") -> str:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
    panels = [
        ("EC_uS_cm", "Electrical Conductivity (µS/cm)"),
        ("pH", "pH"),
        ("DO_mg_L", "Dissolved Oxygen (mg/L)"),
    ]
    for ax, (col, title) in zip(axes, panels):
        ax.bar(df["Basin"], df[col], color="#2a7fba")
        ax.set_title(title)
        ax.tick_params(axis="x", rotation=30)
    plt.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def _main():
    parser = argparse.ArgumentParser(description="Water-quality index engine (EC, pH, DO) for river basins.")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--out", type=str, default="water_quality.png")
    args = parser.parse_args()

    df = generate_synthetic_water_quality(seed=args.seed)
    df["WQI_composite"] = df.apply(composite_water_quality_index, axis=1)
    print(df.to_string(index=False))
    out_path = plot_water_quality(df, args.out)
    print(f"\nChart saved to {out_path}")


if __name__ == "__main__":
    _main()
