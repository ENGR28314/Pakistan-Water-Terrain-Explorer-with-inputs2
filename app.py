"""
app.py
Pakistan Water, Terrain & Disaster-Risk Explorer
A Streamlit dashboard covering provinces, rivers, dams/barrages, link canals,
climatic regions, mountain ranges, national disaster-risk context, lakes,
socio-economic & agro-economic domains, and the geo-political / strategic
water dimension (Indus Waters Treaty, inter-provincial disputes, CPEC
hydropower investment, and India's upstream dam-design disputes).

Run with:  streamlit run app.py
"""

import streamlit as st
import pandas as pd

import data_loader as data
import map_view
import network_view
import hydraulic_model as hm
import file_import

st.set_page_config(
    page_title="Pakistan Water, Terrain & Disaster-Risk Explorer",
    page_icon="🇵🇰 Pakistan",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------------------------
SECTIONS = [
    "🏠 Overview",
    "🗺️ Provinces",
    "🌊 Rivers",
    "🚧 Dams & Barrages",
    "🔀 Link Canals",
    "🌡️ Climatic Regions",
    "⛰️ Mountain Ranges",
    "🏞️ Lakes",
    "🏜️ Deserts",
    "⚠️ Disaster Risk Context",
    "📈 Socio-Economic & Agro-Economic",
    "🗺️ Geo-Political & Strategic",
    "🇨🇳 China Hydropower (CPEC)",
    "📐 India Upstream Dam Disputes",
    "🧮 Interactive Hydraulic Models",
    "📤 Upload File → Map",
    "📚 Sources",
]

st.sidebar.title("🇵🇰")
choice = st.sidebar.radio("Go to section", SECTIONS, label_visibility="collapsed")
st.sidebar.markdown("---")
st.sidebar.caption(
    "Educational dashboard. Figures are curated summaries — verify against "
    "WAPDA, IRSA, PMD, NDMA/PDMA and the Indus Waters Treaty text before "
    "using in formal reports."
)

# ---------------------------------------------------------------------------
# 🏠 OVERVIEW
# ---------------------------------------------------------------------------
if choice == "🏠 Overview":
    st.title("Pakistan Water, Terrain & Disaster-Risk Explorer")
    st.markdown(
        "**An Interactive reference dashboard covering Pakistan's** **provinces**, "
        "**river systems**, **dams/barrages/link canals**, **climatic regions**, "
        "**mountain ranges**, **national disaster-risk context**, **lakes**, **and the** "
        "**socio-economic, agro-economic and geo-political dimensions** **of water "
        "management** **— including the** **Indus Waters Treaty**, **Inter-provincial disputes**, "
        "**CPEC hydropower investment, and India's upstream dam-design disputes**."  "*****(By Engr. Syed Hassan Iqbal Shah)***** "
    )
    st.plotly_chart(map_view.combined_overview_map(), use_container_width=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Provinces / Territories", len(data.PROVINCES))
    col2.metric("Major Rivers Tracked", len(data.RIVERS))
    col3.metric("Dams / Barrages / Hydropower", len(data.DAMS_BARRAGES))
    col4.metric("Link Canals", len(data.LINK_CANALS))

    st.markdown("### What's inside")
    st.markdown(
        "- **Provinces** — Gilgit-Baltistan, KPK, Punjab, Sindh, Balochistan, AJK, ICT\n"
        "- **Rivers** — source, upstream/downstream path, confluences, associated infrastructure\n"
        "- **Dams, Barrages & Link Canals** — the Indus Basin Irrigation System (IBIS)\n"
        "- **Climatic Regions** — Temperate, Tropical, Polar, Arid, Highland\n"
        "- **Mountain Ranges** — Karakoram, Himalayas, Hindu Kush, Hindu Raj, Spin Ghar, "
        "Sulaiman, Kirthar, Toba Kakar, Salt Range — peaks, geology, tourism, climbing\n"
        "- **Deserts** — Thar, Cholistan, Kharan, Thal and the Katpana cold desert, with "
        "approximate mapped extents\n"
        "- **National Disaster Risk Context** — hazard profile, exposure/vulnerability, "
        "emerging risks (GLOFs, monsoon variability, sea intrusion), risk scenarios\n"
        "- **Socio-Economic & Agro-Economic Domains** — food security, IBIS, GDP linkages\n"
        "- **Geo-Political & Strategic** — Kashmir hydro-politics, IWT, inter-provincial "
        "disputes (Punjab vs Sindh), IRSA/CCI legal mechanisms\n"
        "- **China's CPEC Hydropower Footprint** — Karot, Suki Kinari, Kohala, Azad Pattan\n"
        "- **India's Upstream Dam Disputes** — Pakal Dul & Ratle technical contentions\n"
        "- **Interactive Hydraulic Models** — simplified reservoir, shortage-sharing, "
        "link-canal transfer and disaster-risk-index calculators"
    )
    st.caption(
        "Geopolitical, CPEC and dam-governance content is backed by official sources — "
        "see the **📚 Sources** section in the sidebar."
    )

# ---------------------------------------------------------------------------
# 🗺️ PROVINCES
# ---------------------------------------------------------------------------
elif choice == "🗺️ Provinces":
    st.title("Provinces & Territories of Pakistan")
    st.plotly_chart(map_view.province_overview_map(), use_container_width=True)

    prov_name = st.selectbox("Select a province / territory", list(data.PROVINCES.keys()))
    p = data.PROVINCES[prov_name]
    c1, c2 = st.columns([2, 1])
    with c1:
        st.subheader(prov_name)
        st.write(p["overview"])
        st.markdown(f"**Major rivers:** {', '.join(p['major_rivers']) or '—'}")
        st.markdown(f"**Major dams / barrages:** {', '.join(p['major_dams_barrages']) or '—'}")
        st.markdown(f"**Climatic regions:** {', '.join(p['climate_regions'])}")
        st.markdown(f"**Mountain ranges:** {', '.join(p['mountain_ranges']) or '—'}")
        st.markdown(f"**Key lakes:** {', '.join(p['key_lakes']) or '—'}")
    with c2:
        st.metric("Capital", p["capital"])
        st.metric("Area (km²)", f"{p['area_km2']:,}")

    st.markdown("### All provinces at a glance")
    df = pd.DataFrame([
        {
            "Province": k,
            "Capital": v["capital"],
            "Area (km²)": v["area_km2"],
            "Major Rivers": ", ".join(v["major_rivers"]),
            "Climatic Regions": ", ".join(v["climate_regions"]),
        }
        for k, v in data.PROVINCES.items()
    ])
    st.dataframe(df, use_container_width=True, hide_index=True)

# ---------------------------------------------------------------------------
# 🌊 RIVERS
# ---------------------------------------------------------------------------
elif choice == "🌊 Rivers":
    st.title("Rivers of Pakistan")
    all_rivers = list(data.RIVERS.keys())
    selected = st.multiselect("Filter rivers on the map", all_rivers, default=all_rivers)
    st.plotly_chart(map_view.rivers_map(selected), use_container_width=True)

    river_name = st.selectbox("Select a river for details", all_rivers)
    r = data.RIVERS[river_name]
    c1, c2 = st.columns(2)
    with c1:
        st.subheader(river_name)
        st.markdown(f"**Length:** {r['length_km']} km")
        st.markdown(f"**Source:** {r['source']}")
        st.markdown(f"**Upstream path:** {r['upstream']}")
        st.markdown(f"**Downstream path:** {r['downstream']}")
    with c2:
        st.markdown("**River confluences:**")
        for c in r["confluences"]:
            st.markdown(f"- {c}")
        st.markdown(f"**Provinces traversed:** {', '.join(r['provinces'])}")
        st.markdown(f"**Associated dams/barrages:** {', '.join(r['dams_barrages']) or '—'}")
        if r.get("notes"):
            st.info(r["notes"])

    st.markdown("### River confluence network (schematic)")
    st.plotly_chart(network_view.river_confluence_network(), use_container_width=True)

    st.markdown("### River confluence points (interactive map)")
    st.plotly_chart(map_view.river_confluence_geomap(), use_container_width=True)

# ---------------------------------------------------------------------------
# 🚧 DAMS & BARRAGES
# ---------------------------------------------------------------------------
elif choice == "🚧 Dams & Barrages":
    st.title("Dams, Barrages & Hydropower Projects")
    all_names = list(data.DAMS_BARRAGES.keys())
    selected = st.multiselect("Filter on the map", all_names, default=all_names)
    st.plotly_chart(map_view.dams_barrages_map(selected), use_container_width=True)

    df = pd.DataFrame([
        {"Name": k, **v} for k, v in data.DAMS_BARRAGES.items()
    ]).rename(columns={
        "type": "Type", "river": "River", "province": "Province",
        "year_completed": "Year Completed", "capacity_MW": "Capacity (MW)", "purpose": "Purpose",
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown("### Irrigation & hydropower network (schematic)")
    st.plotly_chart(network_view.irrigation_network_diagram(), use_container_width=True)

    st.markdown("### Irrigation & hydropower network (interactive map)")
    st.plotly_chart(map_view.irrigation_network_geomap(), use_container_width=True)

    with st.expander("📚 Sources for this section"):
        for ref in data.SOURCES["Dams & Water Governance"] + data.SOURCES["Indus Basin Irrigation System"]:
            st.markdown(f"- [{ref['label']}]({ref['url']})")

# ---------------------------------------------------------------------------
# 🔀 LINK CANALS
# ---------------------------------------------------------------------------
elif choice == "🔀 Link Canals":
    st.title("Link Canals — Indus Basin Irrigation System (IBIS)")
    st.markdown(
        "Link canals move surplus water between rivers to compensate zones "
        "(especially the Ravi and Sutlej commands) whose natural flows were "
        "reduced after the eastern rivers were allocated to India under the "
        "1960 Indus Waters Treaty."
    )
    st.plotly_chart(map_view.link_canals_map(), use_container_width=True)

    for name, info in data.LINK_CANALS.items():
        with st.expander(name):
            st.markdown(f"**Connects:** {info['connects']}")
            st.markdown(f"**Province:** {info['province']}")
            st.markdown(f"**Purpose:** {info['purpose']}")

# ---------------------------------------------------------------------------
# 🌡️ CLIMATIC REGIONS
# ---------------------------------------------------------------------------
elif choice == "🌡️ Climatic Regions":
    st.title("Climatic Regions of Pakistan")
    st.plotly_chart(map_view.climatic_regions_map(), use_container_width=True)

    cols = st.columns(len(data.CLIMATIC_REGIONS))
    for col, (region, info) in zip(cols, data.CLIMATIC_REGIONS.items()):
        with col:
            st.subheader(region)
            st.markdown(f"**Areas:** {', '.join(info['areas'])}")
            st.caption(info["characteristics"])

    st.markdown("### Which provinces fall in which climatic region?")
    rows = []
    for prov, p in data.PROVINCES.items():
        for region in p["climate_regions"]:
            rows.append({"Province": prov, "Climatic Region": region})
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

# ---------------------------------------------------------------------------
# ⛰️ MOUNTAIN RANGES
# ---------------------------------------------------------------------------
elif choice == "⛰️ Mountain Ranges":
    st.title("Mountain Ranges of Pakistan")
    st.plotly_chart(map_view.mountains_map(), use_container_width=True)

    for group_name, ranges in data.MOUNTAIN_RANGES.items():
        st.header(group_name)
        range_name = st.selectbox(
            f"Select a range in '{group_name}'", list(ranges.keys()), key=group_name
        )
        r = ranges[range_name]
        st.subheader(range_name)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"**Highest peak:** {r['highest_peak']}")
            if r.get("other_notable_peaks"):
                st.markdown("**Other notable peaks:**")
                peaks_df = pd.DataFrame(r["other_notable_peaks"]).rename(
                    columns={"name": "Peak", "elevation_m": "Elevation (m)"}
                )
                st.dataframe(peaks_df, use_container_width=True, hide_index=True)
            st.markdown(f"**Surrounding areas:** {r['surrounding_areas']}")
            st.markdown(f"**Rivers flowing through / from this range:** {', '.join(r['rivers'])}")
            st.markdown(f"**Access towns:** {', '.join(r.get('access_towns', [])) or '—'}")
        with c2:
            st.markdown(f"**Climbing details:** {r['climbing_details']}")
            st.markdown(f"**Best climbing/trekking season:** {r.get('best_climbing_season', '—')}")
            st.markdown(f"**Permits required:** {r.get('permits_required', '—')}")
            if r.get("trekking_routes"):
                st.markdown("**Popular trekking routes:**")
                for route in r["trekking_routes"]:
                    st.markdown(f"- {route}")
            if r.get("hazards"):
                st.warning(f"**Hazards:** {r['hazards']}")

        st.markdown(f"**Geology:** {r['geology']}")
        st.markdown(f"**Tourist guide:** {r['tourist_guide']}")
        st.markdown("---")

# ---------------------------------------------------------------------------
# 🏞️ LAKES
# ---------------------------------------------------------------------------
elif choice == "🏞️ Lakes":
    st.title("Lakes of Pakistan")
    st.plotly_chart(map_view.lakes_map(), use_container_width=True)
    df = pd.DataFrame([{"Lake": k, **v} for k, v in data.LAKES.items()]).rename(
        columns={"province": "Province", "formation": "Formation", "type": "Type"}
    )
    st.dataframe(df, use_container_width=True, hide_index=True)

# ---------------------------------------------------------------------------
# 🏜️ DESERTS
# ---------------------------------------------------------------------------
elif choice == "🏜️ Deserts":
    st.title("Deserts of Pakistan")
    st.plotly_chart(map_view.deserts_map(), use_container_width=True)

    df = pd.DataFrame([
        {
            "Desert": k,
            "Province": v["province"],
            "Area (km²)": v["area_km2"] if v["area_km2"] else "—",
            "Type": v["type"],
        }
        for k, v in data.DESERTS.items()
    ])
    st.dataframe(df, use_container_width=True, hide_index=True)

    desert_name = st.selectbox("Select a desert for details", list(data.DESERTS.keys()))
    d = data.DESERTS[desert_name]
    st.subheader(desert_name)
    st.markdown(f"**Province:** {d['province']}")
    area_text = f"{d['area_km2']:,} km²" if d["area_km2"] else "Not well-documented (localized dune field)"
    st.markdown(f"**Approximate area:** {area_text}")
    st.markdown(f"**Type:** {d['type']}")
    st.write(d["characteristics"])

# ---------------------------------------------------------------------------
# ⚠️ DISASTER RISK CONTEXT
# ---------------------------------------------------------------------------
elif choice == "⚠️ Disaster Risk Context":
    st.title("National Disaster Risk Context")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["1. Hazard Profile", "2. Exposure & Vulnerability", "3. Emerging Risks",
         "4. Risk Scenarios", "5. Historical Events & Hazard Map"]
    )

    with tab1:
        for category, hazards in data.DISASTER_HAZARD_PROFILE.items():
            st.subheader(category)
            for hazard, detail in hazards.items():
                if isinstance(detail, dict):
                    with st.expander(hazard):
                        for sub, subdetail in detail.items():
                            st.markdown(f"**{sub}:** {subdetail}")
                else:
                    st.markdown(f"**{hazard}:** {detail}")
            st.markdown("---")

    with tab2:
        for factor, detail in data.DISASTER_EXPOSURE_VULNERABILITY.items():
            st.subheader(factor)
            if isinstance(detail, dict):
                if "drivers" in detail:
                    st.markdown(", ".join(detail["drivers"]))
                    st.caption(detail["summary"])
                else:
                    for sub, subdetail in detail.items():
                        st.markdown(f"**{sub}:** {subdetail}")
            else:
                st.write(detail)

    with tab3:
        for topic, detail in data.DISASTER_EMERGING_RISKS.items():
            st.subheader(topic)
            st.write(detail)

    with tab4:
        cols = st.columns(3)
        for col, (scenario, info) in zip(cols, data.DISASTER_RISK_SCENARIOS.items()):
            with col:
                st.subheader(scenario)
                st.write(info["description"])
                for feat in info["features"]:
                    st.markdown(f"- {feat}")

    with tab5:
        st.subheader("Historical Disaster Timeline")
        st.plotly_chart(map_view.historical_events_map(), use_container_width=True)

        hist_df = pd.DataFrame(data.DISASTER_HISTORICAL_EVENTS)
        hist_df["provinces"] = hist_df["provinces"].apply(lambda x: ", ".join(x))
        hist_df = hist_df.rename(columns={
            "year": "Year", "name": "Event", "hazard_type": "Hazard Type",
            "provinces": "Provinces Affected", "summary": "Summary",
        })
        st.dataframe(hist_df, use_container_width=True, hide_index=True)

        year_min, year_max = int(hist_df["Year"].min()), int(hist_df["Year"].max())
        year_range = st.slider("Filter by year", year_min, year_max, (year_min, year_max))
        filtered = hist_df[(hist_df["Year"] >= year_range[0]) & (hist_df["Year"] <= year_range[1])]
        for _, row in filtered.iterrows():
            with st.expander(f"{row['Year']} — {row['Event']} ({row['Hazard Type']})"):
                st.markdown(f"**Provinces affected:** {row['Provinces Affected']}")
                st.write(row["Summary"])

        st.markdown("---")
        st.subheader("Dominant Hazards by Province")
        prov_choice = st.selectbox("Select a province / territory", list(data.DISASTER_HAZARD_BY_PROVINCE.keys()))
        for hz in data.DISASTER_HAZARD_BY_PROVINCE[prov_choice]:
            st.markdown(f"- {hz}")

# ---------------------------------------------------------------------------
# 📈 SOCIO-ECONOMIC & AGRO-ECONOMIC
# ---------------------------------------------------------------------------
elif choice == "📈 Socio-Economic & Agro-Economic":
    st.title("Socio-Economic & Agro-Economic Domains")

    st.header("📈 Socio-Economic Domain")
    for k, v in data.SOCIO_ECONOMIC_DOMAIN.items():
        st.markdown(f"**{k}:** {v}")

    st.header("🌾 Agro-Economic Domain")
    for k, v in data.AGRO_ECONOMIC_DOMAIN.items():
        st.markdown(f"**{k}:** {v}")

# ---------------------------------------------------------------------------
# 🗺️ GEO-POLITICAL & STRATEGIC
# ---------------------------------------------------------------------------
elif choice == "🗺️ Geo-Political & Strategic":
    st.title("Geo-Political & Strategic Domains")
    st.plotly_chart(map_view.geopolitical_map(), use_container_width=True)

    st.header("🗺️ Strategic Overview")
    for k, v in data.GEOPOLITICAL_DOMAIN.items():
        with st.expander(k):
            st.write(v)

    st.header("⚖️ Internal Inter-Provincial Water Disputes: Punjab vs. Sindh")
    d = data.INTERNAL_WATER_DISPUTES
    st.write(d["overview"])
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Sindh's Grievances (Lower Riparian)")
        st.write(d["Sindh's Grievances (Lower Riparian)"])
    with c2:
        st.subheader("Punjab's Counter-Claims (Upper Riparian)")
        st.write(d["Punjab's Counter-Claims (Upper Riparian)"])
    st.subheader("Structural Gridlocks / Deadlock")
    st.write(d["Structural Gridlocks / Deadlock"])
    st.subheader("Environmental Impacts of Indian Chenab Projects on Punjab's Crops")
    for k, v in d["Environmental Impacts of Indian Chenab Projects on Punjab's Crops"].items():
        st.markdown(f"**{k}:** {v}")

    st.header("⚖️ Legal Mechanisms to Resolve IRSA Inter-Provincial Disputes")
    for k, v in data.IRSA_LEGAL_MECHANISMS.items():
        st.markdown(f"**{k}:** {v}")

    with st.expander("📚 Sources for this section"):
        for ref in data.SOURCES["Indus Waters Treaty & Arbitration"] + data.SOURCES["Dams & Water Governance"]:
            st.markdown(f"- [{ref['label']}]({ref['url']})")

# ---------------------------------------------------------------------------
# 🇨🇳 CHINA HYDROPOWER (CPEC)
# ---------------------------------------------------------------------------
elif choice == "🇨🇳 China Hydropower (CPEC)":
    st.title("The Financial Footprint of China's Investments in Pakistan's Hydropower")
    st.plotly_chart(map_view.china_hydropower_map(), use_container_width=True)

    fp = data.CHINA_HYDROPOWER_FOOTPRINT
    st.markdown(f"**Dominant share of FDI:** {fp['Dominant Share of FDI']}")

    st.subheader("Major Hydropower Asset Portfolio")
    df = pd.DataFrame([
        {"Project": k, **v} for k, v in fp["Major Hydropower Asset Portfolio"].items()
    ]).rename(columns={
        "capacity_MW": "Capacity (MW)", "river": "River", "status": "Status", "notes": "Notes",
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

    total_mw = sum(v["capacity_MW"] for v in fp["Major Hydropower Asset Portfolio"].values())
    st.metric("Combined CPEC hydropower capacity (portfolio total)", f"{total_mw:,.1f} MW")

    st.markdown("### Portfolio network by host river")
    st.plotly_chart(network_view.hydropower_cpec_network(), use_container_width=True)

    with st.expander("📚 Sources for this section"):
        for ref in data.SOURCES["CPEC Hydropower Projects"]:
            st.markdown(f"- [{ref['label']}]({ref['url']})")

# ---------------------------------------------------------------------------
# 📐 INDIA UPSTREAM DAM DISPUTES
# ---------------------------------------------------------------------------
elif choice == "📐 India Upstream Dam Disputes":
    st.title("Objectionable Technical Designs of India's Pakal Dul & Ratle Dams")
    st.plotly_chart(map_view.india_dam_disputes_map(), use_container_width=True)

    dd = data.INDIA_DAM_DESIGN_DISPUTES

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Pakal Dul Dam")
        st.metric("Capacity", f"{dd['Pakal Dul Dam']['capacity_MW']} MW")
        st.markdown(f"**River:** {dd['Pakal Dul Dam']['river']}")
        st.markdown(f"**Location:** {dd['Pakal Dul Dam']['location']}")
    with c2:
        st.subheader("Ratle Dam")
        st.metric("Capacity", f"{dd['Ratle Dam']['capacity_MW']} MW")
        st.markdown(f"**River:** {dd['Ratle Dam']['river']}")
        st.markdown(f"**Location:** {dd['Ratle Dam']['location']}")

    st.header("Technical Points of Contention")
    tp = dd["technical_points_of_contention"]
    for topic in ["Pondage Capacity", "Freeboard Height & Dam Elevation", "Deep-Level Outlets and Gated Spillways"]:
        with st.expander(topic):
            st.markdown(f"**The issue:** {tp[topic]['issue']}")
            st.markdown(f"**Pakistan's view:** {tp[topic]['pakistan_view']}")

    st.subheader("Court of Arbitration (CoA) Interventions")
    st.write(tp["Court of Arbitration (CoA) Interventions"])

    with st.expander("📚 Sources for this section"):
        for ref in data.SOURCES["Indus Waters Treaty & Arbitration"]:
            st.markdown(f"- [{ref['label']}]({ref['url']})")

# ---------------------------------------------------------------------------
# 🧮 INTERACTIVE HYDRAULIC MODELS
# ---------------------------------------------------------------------------
elif choice == "🧮 Interactive Hydraulic Models":
    st.title("Interactive Hydraulic & Risk Models")
    st.caption(
        "⚠️ Simplified, illustrative models for dashboard exploration only — "
        "not validated hydrological/engineering tools."
    )

    with st.expander("📍 Reference map — real infrastructure these models are inspired by", expanded=False):
        st.plotly_chart(map_view.irrigation_network_geomap(), use_container_width=True)
        st.caption(
            "The reservoir, shortage-sharing, link-canal and risk-index tools below use "
            "generic user-entered numbers — this map just shows where the real dams, "
            "barrages and link canals they're modeled on actually sit."
        )

    model_tab1, model_tab2, model_tab3, model_tab4 = st.tabs(
        ["Reservoir Simulation", "Shortage-Sharing Allocation", "Link Canal Transfer", "Disaster Risk Index"]
    )

    with model_tab1:
        st.subheader("Simplified Reservoir Mass-Balance Simulation")
        c1, c2 = st.columns(2)
        with c1:
            capacity = st.number_input("Live storage capacity (MAF)", value=6.8, min_value=0.1)
            current = st.number_input("Current storage (MAF)", value=3.0, min_value=0.0)
        with c2:
            inflow = st.number_input("Inflow (cusecs)", value=150000, step=1000)
            outflow = st.number_input("Outflow / demand (cusecs)", value=120000, step=1000)
        days = st.slider("Simulation horizon (days)", 5, 120, 30)

        state = hm.ReservoirState("Reservoir", capacity, current, inflow, outflow)
        trace = hm.simulate_reservoir(state, days)
        df = pd.DataFrame(trace)
        st.line_chart(df.set_index("day")["storage_maf"])
        if df["spilling"].any():
            st.warning("Reservoir reaches full capacity and begins spilling during this simulation.")
        st.dataframe(df, use_container_width=True, hide_index=True)

    with model_tab2:
        st.subheader("Simplified Shortage-Sharing Allocation")
        st.caption("Illustrative equal-percentage shortage-sharing model — not the official IRSA formula.")
        total = st.number_input("Total available water (MAF)", value=100.0, min_value=0.0)
        shortage = st.slider("System-wide shortage (%)", 0, 50, 10)
        alloc = hm.allocate_shortage(total, shortage)
        st.bar_chart(pd.Series(alloc, name="Allocation (MAF)"))
        st.dataframe(
            pd.DataFrame(alloc.items(), columns=["Province", "Allocation (MAF)"]),
            use_container_width=True, hide_index=True,
        )

    with model_tab3:
        st.subheader("Link Canal Transfer Calculator")
        c1, c2, c3 = st.columns(3)
        with c1:
            src_flow = st.number_input("Source river flow (cusecs)", value=50000, step=1000)
        with c2:
            canal_cap = st.number_input("Link canal capacity (cusecs)", value=15000, step=500)
        with c3:
            offtake = st.slider("Requested offtake (% of source flow)", 0, 100, 40)
        result = hm.link_canal_transfer(src_flow, canal_cap, offtake)
        c1, c2, c3 = st.columns(3)
        c1.metric("Requested (cusecs)", f"{result['requested_cusecs']:,.0f}")
        c2.metric("Transferred (cusecs)", f"{result['transferred_cusecs']:,.0f}")
        c3.metric("Remaining in source river (cusecs)", f"{result['remaining_in_source_river_cusecs']:,.0f}")
        if result["capacity_limited"]:
            st.info("Transfer is capped by the link canal's design capacity, not the offtake request.")

    with model_tab4:
        st.subheader("Composite Disaster Risk Index (illustrative)")
        c1, c2, c3 = st.columns(3)
        with c1:
            flood = st.slider("Flood exposure", 0, 10, 7)
            glof = st.slider("GLOF susceptibility", 0, 10, 6)
        with c2:
            drought = st.slider("Drought exposure", 0, 10, 5)
            seismic = st.slider("Seismic hazard", 0, 10, 7)
        with c3:
            coastal = st.slider("Coastal exposure", 0, 10, 4)
            capacity_score = st.slider("Institutional capacity (higher = better)", 0, 10, 4)

        score, band = hm.composite_disaster_risk_index(flood, glof, drought, seismic, coastal, capacity_score)
        st.metric("Composite Risk Score (0-100)", score, delta=band)
        band_colors = {"Low": "🟢", "Moderate": "🟡", "High": "🟠", "Severe": "🔴"}
        st.markdown(f"### {band_colors.get(band, '')} Risk Band: **{band}**")

# ---------------------------------------------------------------------------
# 📤 UPLOAD FILE → MAP
# ---------------------------------------------------------------------------
elif choice == "📤 Upload File → Map":
    st.title("Upload Your Own Data → Map")
    st.caption(
        "Upload a CSV or PDF with location data and it will be plotted on an "
        "interactive map — no coding required."
    )
    with st.expander("📋 Expected file format", expanded=False):
        st.markdown(
            "**CSV:** a table with latitude/longitude columns, using headers such as "
            "`lat`/`latitude` and `lon`/`longitude` (or `lng`, `x`, `y`). An optional "
            "`name` (or `label`/`place`/`site`) column is used for point labels, and an "
            "optional `category` (or `type`/`group`) column will color-code the points.\n\n"
            "**PDF:** either a table using the same kind of column headers, or plain text "
            "containing coordinate pairs on their own lines, e.g. `Site A: 31.52, 74.35` "
            "or `31.52N, 74.35E`."
        )
        example_df = pd.DataFrame({
            "name": ["Islamabad", "Karachi", "Lahore"],
            "lat": [33.70, 24.86, 31.55],
            "lon": [73.10, 67.01, 74.35],
            "category": ["Capital", "Port City", "Capital"],
        })
        st.dataframe(example_df, use_container_width=True, hide_index=True)
        st.download_button(
            "Download example CSV",
            example_df.to_csv(index=False).encode("utf-8"),
            file_name="example_locations.csv",
            mime="text/csv",
        )

    uploaded_file = st.file_uploader("Choose a CSV or PDF file", type=["csv", "pdf"])

    if uploaded_file is not None:
        try:
            df_points = file_import.load_any(uploaded_file)
        except file_import.FileImportError as e:
            st.error(str(e))
        else:
            st.success(f"Parsed {len(df_points)} location(s) from **{uploaded_file.name}**.")
            st.plotly_chart(
                map_view.custom_points_map(df_points, title=f"Map — {uploaded_file.name}"),
                use_container_width=True,
            )
            st.dataframe(df_points, use_container_width=True, hide_index=True)
            st.download_button(
                "Download parsed data as CSV",
                df_points.to_csv(index=False).encode("utf-8"),
                file_name="parsed_locations.csv",
                mime="text/csv",
            )
    else:
        st.info("No file uploaded yet — showing the example data above on a map.")
        example_df = pd.DataFrame({
            "Name": ["Islamabad", "Karachi", "Lahore"],
            "Latitude": [33.70, 24.86, 31.55],
            "Longitude": [73.10, 67.01, 74.35],
            "Category": ["Capital", "Port City", "Capital"],
        })
        st.plotly_chart(
            map_view.custom_points_map(example_df, title="Example — Pakistani Cities"),
            use_container_width=True,
        )

# ---------------------------------------------------------------------------
# 📚 SOURCES
# ---------------------------------------------------------------------------
elif choice == "📚 Sources":
    st.title("📚 Sources")
    st.caption(
        "Primary and official references behind the geopolitical, CPEC, dam-governance "
        "and Indus Basin Irrigation System content in this dashboard. Everything else "
        "(rivers, mountains, lakes, deserts, climate regions, coordinates) is a curated "
        "summary for visualization — see the accuracy note on the Overview page."
    )
    for topic, refs in data.SOURCES.items():
        st.subheader(topic)
        for ref in refs:
            st.markdown(f"- [{ref['label']}]({ref['url']})")

st.sidebar.markdown("---")
st.sidebar.caption("Built with Streamlit · Plotly · NetworkX")
