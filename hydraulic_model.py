"""
hydraulic_model.py
Simplified, transparent illustrative models — NOT a validated hydrological
or hydraulic simulator. Intended to give dashboard users an interactive
feel for how storage, canal offtake and shortage-sharing work in the
Indus Basin system, and a basic composite disaster-risk-index calculator.

All coefficients are illustrative approximations for teaching/dashboard
purposes and should not be used for engineering or policy decisions.
"""

from dataclasses import dataclass


# ---------------------------------------------------------------------------
# 1. SIMPLE RESERVOIR MASS-BALANCE MODEL (Tarbela / Mangla style)
# ---------------------------------------------------------------------------
@dataclass
class ReservoirState:
    name: str
    capacity_maf: float          # live storage capacity, million acre-feet
    current_storage_maf: float
    inflow_cusecs: float         # cubic feet per second
    outflow_demand_cusecs: float


def simulate_reservoir(state: ReservoirState, days: int = 30):
    """
    Very simplified daily mass-balance: storage change = (inflow - outflow) * dt
    converted from cusecs to MAF/day. 1 cusec-day ≈ 0.00198347 acre-feet.
    Returns a list of (day, storage_maf, spill_flag).
    """
    cusec_day_to_af = 1.98347 / 1000.0  # acre-feet per cusec-day
    storage = state.current_storage_maf
    trace = []
    for day in range(1, days + 1):
        net_cusecs = state.inflow_cusecs - state.outflow_demand_cusecs
        delta_af = net_cusecs * cusec_day_to_af
        delta_maf = delta_af / 1_000_000
        storage += delta_maf
        spill = False
        if storage > state.capacity_maf:
            storage = state.capacity_maf
            spill = True
        if storage < 0:
            storage = 0
        trace.append({"day": day, "storage_maf": round(storage, 3), "spilling": spill})
    return trace


# ---------------------------------------------------------------------------
# 2. SHORTAGE-SHARING ALLOCATION (simplified 1991 Water Apportionment logic)
# ---------------------------------------------------------------------------
# Illustrative baseline shares, roughly reflecting historical Kharif/Rabi
# apportionment discussions (NOT the official IRSA formula, simplified for demo).
BASELINE_SHARE_PCT = {
    "Punjab": 0.53,
    "Sindh": 0.42,
    "KPK": 0.03,
    "Balochistan": 0.02,
}


def allocate_shortage(total_available_maf: float, shortage_pct: float = 0.0):
    """
    Distributes total_available_maf across provinces using baseline shares.
    shortage_pct (0-100) applies an equal percentage cut to all provinces,
    mirroring Pakistan's (contested) principle of equal-percentage shortage-sharing.
    """
    effective_total = total_available_maf * (1 - shortage_pct / 100.0)
    return {
        province: round(effective_total * share, 3)
        for province, share in BASELINE_SHARE_PCT.items()
    }


# ---------------------------------------------------------------------------
# 3. COMPOSITE DISASTER RISK INDEX (illustrative, 0-100 scale)
# ---------------------------------------------------------------------------
def composite_disaster_risk_index(
    flood_exposure: float,       # 0-10
    glof_susceptibility: float,  # 0-10
    drought_exposure: float,     # 0-10
    seismic_hazard: float,       # 0-10
    coastal_exposure: float,     # 0-10
    institutional_capacity: float,  # 0-10 (higher = better prepared, reduces risk)
):
    """
    Weighted composite index (illustrative only).
    Risk = weighted hazard sum, adjusted downward by institutional capacity.
    Returns a score 0-100 and a qualitative band.
    """
    hazard_score = (
        0.25 * flood_exposure
        + 0.20 * glof_susceptibility
        + 0.20 * drought_exposure
        + 0.15 * seismic_hazard
        + 0.20 * coastal_exposure
    )  # max 10
    capacity_adjustment = 1 - (institutional_capacity / 20.0)  # 0.5-1.0 multiplier
    raw_score = hazard_score * 10 * capacity_adjustment  # scale to 0-100
    raw_score = max(0, min(100, raw_score))

    if raw_score < 25:
        band = "Low"
    elif raw_score < 50:
        band = "Moderate"
    elif raw_score < 75:
        band = "High"
    else:
        band = "Severe"

    return round(raw_score, 1), band


# ---------------------------------------------------------------------------
# 4. LINK CANAL TRANSFER CALCULATOR
# ---------------------------------------------------------------------------
def link_canal_transfer(source_flow_cusecs: float, canal_capacity_cusecs: float, offtake_pct: float):
    """
    Simplified transfer through a link canal: transfer is capped by both
    the canal's design capacity and the requested offtake percentage of
    the source river's flow.
    """
    requested = source_flow_cusecs * (offtake_pct / 100.0)
    transferred = min(requested, canal_capacity_cusecs)
    remaining_in_river = source_flow_cusecs - transferred
    return {
        "requested_cusecs": round(requested, 1),
        "transferred_cusecs": round(transferred, 1),
        "remaining_in_source_river_cusecs": round(remaining_in_river, 1),
        "capacity_limited": requested > canal_capacity_cusecs,
    }
