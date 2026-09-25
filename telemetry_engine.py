"""
telemetry_engine.py
Standalone simulation/visualization engine for river-basin telemetry data
(daily gauge/discharge-style readings). Analyzes which basin reports the
highest average telemetry variance.

Context: under the Indus Waters Treaty (IWT) Article VI, Pakistan and India
exchange daily gauge/discharge readings, reservoir releases and canal
withdrawals through the Permanent Indus Commission (PIC). Real PIC-exchanged
telemetry isn't publicly published, so this engine generates a clearly
illustrative/synthetic daily discharge series per basin to demonstrate the
variance-analysis workflow — the same functions work unchanged on a real
telemetry CSV (Date, Basin, Discharge_cumecs columns) once one is available,
including via the app's Upload File → Map & Charts tab.

Run standalone:
    python telemetry_engine.py --days 90 --seed 7 --out telemetry_variance.png

Or import into the Streamlit app:
    from telemetry_engine import generate_synthetic_telemetry, compute_basin_variance
"""

import argparse

import numpy as np
import pandas as pd

DEFAULT_BASINS = ["Indus", "Jhelum", "Chenab", "Ravi", "Sutlej", "Kabul"]

# Illustrative baseline mean discharge (cumecs) and day-to-day volatility
# factor per basin — loosely reflects relative scale (Indus largest) and
# monsoon-driven flashiness (eastern rivers / Kabul more variable). NOT
# measured or officially reported figures.
_BASIN_PROFILE = {
    "Indus":  {"mean": 5500, "volatility": 0.18},
    "Jhelum": {"mean": 900,  "volatility": 0.30},
    "Chenab": {"mean": 1600, "volatility": 0.28},
    "Ravi":   {"mean": 250,  "volatility": 0.45},
    "Sutlej": {"mean": 300,  "volatility": 0.40},
    "Kabul":  {"mean": 700,  "volatility": 0.35},
}


def generate_synthetic_telemetry(basins=None, days: int = 90, seed=None) -> pd.DataFrame:
    """
    Build an illustrative daily discharge telemetry table: one row per
    (date, basin) with a synthetic 'Discharge_cumecs' reading. NOT real
    PIC-exchanged data — for demonstrating the variance-analysis workflow.
    """
    basins = basins or DEFAULT_BASINS
    rng = np.random.default_rng(seed)
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=days, freq="D")

    rows = []
    for basin in basins:
        profile = _BASIN_PROFILE.get(basin, {"mean": 500, "volatility": 0.3})
        mean, vol = profile["mean"], profile["volatility"]
        season = mean * 0.15 * np.sin(np.linspace(0, 3.14, days))
        noise = rng.normal(0, mean * vol, days)
        discharge = np.clip(mean + season + noise, a_min=mean * 0.05, a_max=None)
        for d, val in zip(dates, discharge):
            rows.append({"Date": d, "Basin": basin, "Discharge_cumecs": round(float(val), 1)})
    return pd.DataFrame(rows)


def compute_basin_variance(
    df: pd.DataFrame, value_col: str = "Discharge_cumecs", group_col: str = "Basin"
) -> pd.DataFrame:
    """
    Compute mean, variance, std. dev. and reading count of `value_col` per
    `group_col`, sorted by variance descending (highest-variance basin first).
    Works on any telemetry table with those two columns — synthetic or real.
    """
    summary = (
        df.groupby(group_col)[value_col]
        .agg(mean="mean", variance="var", std="std", n="count")
        .reset_index()
        .sort_values("variance", ascending=False)
        .reset_index(drop=True)
    )
    return summary


def highest_variance_basin(
    df: pd.DataFrame, value_col: str = "Discharge_cumecs", group_col: str = "Basin"
) -> str:
    """Return the name of the basin/group with the highest telemetry variance."""
    summary = compute_basin_variance(df, value_col, group_col)
    if summary.empty:
        raise ValueError("No data to analyze.")
    return summary.iloc[0][group_col]


def plot_basin_variance(
    summary_df: pd.DataFrame, out_path: str = "telemetry_variance.png", group_col: str = "Basin"
) -> str:
    """Render a bar chart of variance by basin with matplotlib and save it to out_path."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ["#d62728" if i == 0 else "#1f77b4" for i in range(len(summary_df))]
    ax.bar(summary_df[group_col], summary_df["variance"], color=colors)
    ax.set_ylabel("Variance (cumecs²)")
    ax.set_xlabel("River Basin")
    ax.set_title("Discharge Telemetry Variance by River Basin")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def _main():
    parser = argparse.ArgumentParser(
        description="Analyze which river basin has the highest telemetry (discharge) variance."
    )
    parser.add_argument("--days", type=int, default=90, help="Number of synthetic daily readings per basin.")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility.")
    parser.add_argument("--out", type=str, default="telemetry_variance.png", help="Output chart path.")
    args = parser.parse_args()

    df = generate_synthetic_telemetry(days=args.days, seed=args.seed)
    summary = compute_basin_variance(df)
    print(summary.to_string(index=False))
    top = summary.iloc[0]
    print(f"\nHighest-variance basin: {top['Basin']} (variance = {top['variance']:.1f}, std = {top['std']:.1f} cumecs)")

    out_path = plot_basin_variance(summary, args.out)
    print(f"Chart saved to {out_path}")


if __name__ == "__main__":
    _main()
