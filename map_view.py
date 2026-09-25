"""
map_view.py
Plotly-based map rendering helpers for the Streamlit app.
Uses plotly.graph_objects with scattergeo/scattermap so no extra
mapping dependency (folium/streamlit-folium) is required.
"""

import plotly.graph_objects as go
from coordinates import (
    PROVINCE_COORDS, RIVER_COORDS, DAM_COORDS, MOUNTAIN_PEAK_COORDS, LAKE_COORDS,
    LINK_CANAL_LINES, CLIMATE_REGION_POINTS, GEOPOLITICAL_COORDS,
    INDIA_DISPUTED_DAM_COORDS, CPEC_HYDROPOWER_NAMES, HISTORICAL_EVENT_COORDS,
    CONFLUENCE_COORDS, DESERT_COORDS, DESERT_OUTLINES, NOTABLE_FOREST_COORDS,
    NATIONAL_PARK_COORDS,
)

PAK_CENTER = {"lat": 30.3753, "lon": 69.3451}


def _base_figure(title: str) -> go.Figure:
    fig = go.Figure()
    fig.update_layout(
        title=title,
        geo=dict(
            scope="asia",
            resolution=50,
            showland=True,
            landcolor="rgb(235, 235, 230)",
            showcountries=True,
            countrycolor="rgb(150,150,150)",
            showlakes=True,
            lakecolor="rgb(180, 210, 235)",
            center=PAK_CENTER,
            projection_scale=5.5,
            showrivers=True,
            rivercolor="rgb(120,170,220)",
        ),
        margin=dict(l=0, r=0, t=40, b=0),
        height=600,
    )
    return fig


def province_overview_map() -> go.Figure:
    fig = _base_figure("Provinces of Pakistan — Capitals")
    lats = [v["lat"] for v in PROVINCE_COORDS.values()]
    lons = [v["lon"] for v in PROVINCE_COORDS.values()]
    names = [f"{k} (Capital: {v['capital']})" for k, v in PROVINCE_COORDS.items()]
    fig.add_trace(go.Scattergeo(
        lat=lats, lon=lons, text=names, mode="markers+text",
        marker=dict(size=14, color="crimson", line=dict(width=1, color="white")),
        textposition="top center", name="Provinces",
    ))
    return fig


def rivers_map(selected_rivers=None) -> go.Figure:
    fig = _base_figure("Major Rivers of Pakistan")
    rivers = RIVER_COORDS if not selected_rivers else {
        k: v for k, v in RIVER_COORDS.items() if k in selected_rivers
    }
    palette = [
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
        "#aec7e8", "#ffbb78", "#98df8a", "#ff9896",
    ]
    for i, (name, points) in enumerate(rivers.items()):
        lats = [p[0] for p in points]
        lons = [p[1] for p in points]
        fig.add_trace(go.Scattergeo(
            lat=lats, lon=lons, mode="lines+markers", name=name,
            line=dict(width=3, color=palette[i % len(palette)]),
            marker=dict(size=4),
        ))
    return fig


def dams_barrages_map(selected=None) -> go.Figure:
    fig = _base_figure("Dams, Barrages & Hydropower Projects")
    items = DAM_COORDS if not selected else {k: v for k, v in DAM_COORDS.items() if k in selected}
    lats = [v["lat"] for v in items.values()]
    lons = [v["lon"] for v in items.values()]
    names = [f"{k} ({v['river']}, {v['province']})" for k, v in items.items()]
    fig.add_trace(go.Scattergeo(
        lat=lats, lon=lons, text=names, mode="markers",
        marker=dict(size=13, color="darkgreen", symbol="triangle-up",
                    line=dict(width=1, color="white")),
        name="Dams / Barrages / Hydropower",
        hovertext=names, hoverinfo="text",
    ))
    return fig


def mountains_map() -> go.Figure:
    fig = _base_figure("Highest Peaks by Mountain Range")
    lats = [v["lat"] for v in MOUNTAIN_PEAK_COORDS.values()]
    lons = [v["lon"] for v in MOUNTAIN_PEAK_COORDS.values()]
    names = [f"{k} — {v['elevation_m']} m" for k, v in MOUNTAIN_PEAK_COORDS.items()]
    fig.add_trace(go.Scattergeo(
        lat=lats, lon=lons, text=names, mode="markers+text",
        marker=dict(size=12, color="saddlebrown", symbol="triangle-up",
                    line=dict(width=1, color="white")),
        textposition="top center", name="Peaks",
    ))
    return fig


def lakes_map() -> go.Figure:
    fig = _base_figure("Lakes of Pakistan")
    lats = [v["lat"] for v in LAKE_COORDS.values()]
    lons = [v["lon"] for v in LAKE_COORDS.values()]
    names = [f"{k} ({v['province']})" for k, v in LAKE_COORDS.items()]
    fig.add_trace(go.Scattergeo(
        lat=lats, lon=lons, text=names, mode="markers",
        marker=dict(size=12, color="dodgerblue", symbol="circle",
                    line=dict(width=1, color="white")),
        hovertext=names, hoverinfo="text", name="Lakes",
    ))
    return fig


def deserts_map() -> go.Figure:
    fig = _base_figure("Deserts of Pakistan")
    # Shaded approximate extent for the deserts that have an outline
    for name, outline in DESERT_OUTLINES.items():
        lats = [p[0] for p in outline]
        lons = [p[1] for p in outline]
        fig.add_trace(go.Scattergeo(
            lat=lats, lon=lons, mode="lines", fill="toself",
            fillcolor="rgba(237, 201, 100, 0.35)",
            line=dict(width=1, color="rgba(180, 140, 40, 0.6)"),
            name=f"{name} (approx. extent)", hoverinfo="name",
        ))
    lats = [v["lat"] for v in DESERT_COORDS.values()]
    lons = [v["lon"] for v in DESERT_COORDS.values()]
    names = [f"{k} ({v['province']})" for k, v in DESERT_COORDS.items()]
    fig.add_trace(go.Scattergeo(
        lat=lats, lon=lons, text=names, mode="markers+text",
        marker=dict(size=13, color="#c68b28", symbol="circle", line=dict(width=1, color="white")),
        textposition="bottom center", name="Deserts", hoverinfo="text",
    ))
    return fig


def combined_overview_map() -> go.Figure:
    """One map layering provinces, rivers, dams and peaks for a quick overview."""
    fig = _base_figure("Pakistan — Combined Water & Terrain Overview")

    for name, points in RIVER_COORDS.items():
        lats = [p[0] for p in points]
        lons = [p[1] for p in points]
        fig.add_trace(go.Scattergeo(
            lat=lats, lon=lons, mode="lines", name=name,
            line=dict(width=2, color="#1f77b4"), showlegend=False,
            hoverinfo="name",
        ))

    dam_lats = [v["lat"] for v in DAM_COORDS.values()]
    dam_lons = [v["lon"] for v in DAM_COORDS.values()]
    dam_names = list(DAM_COORDS.keys())
    fig.add_trace(go.Scattergeo(
        lat=dam_lats, lon=dam_lons, text=dam_names, mode="markers",
        marker=dict(size=9, color="darkgreen", symbol="triangle-up"),
        name="Dams / Barrages", hoverinfo="text",
    ))

    peak_lats = [v["lat"] for v in MOUNTAIN_PEAK_COORDS.values()]
    peak_lons = [v["lon"] for v in MOUNTAIN_PEAK_COORDS.values()]
    peak_names = list(MOUNTAIN_PEAK_COORDS.keys())
    fig.add_trace(go.Scattergeo(
        lat=peak_lats, lon=peak_lons, text=peak_names, mode="markers",
        marker=dict(size=9, color="saddlebrown", symbol="diamond"),
        name="Major Peaks", hoverinfo="text",
    ))

    prov_lats = [v["lat"] for v in PROVINCE_COORDS.values()]
    prov_lons = [v["lon"] for v in PROVINCE_COORDS.values()]
    prov_names = list(PROVINCE_COORDS.keys())
    fig.add_trace(go.Scattergeo(
        lat=prov_lats, lon=prov_lons, text=prov_names, mode="markers",
        marker=dict(size=11, color="crimson", symbol="star"),
        name="Provinces", hoverinfo="text",
    ))

    desert_lats = [v["lat"] for v in DESERT_COORDS.values()]
    desert_lons = [v["lon"] for v in DESERT_COORDS.values()]
    desert_names = list(DESERT_COORDS.keys())
    fig.add_trace(go.Scattergeo(
        lat=desert_lats, lon=desert_lons, text=desert_names, mode="markers",
        marker=dict(size=9, color="#c68b28", symbol="circle"),
        name="Deserts", hoverinfo="text",
    ))
    return fig


def climatic_regions_map() -> go.Figure:
    fig = _base_figure("Climatic Regions of Pakistan")
    palette = {
        "Temperate": "#2ca02c", "Tropical": "#ff7f0e", "Polar": "#17becf",
        "Arid": "#d62728", "Highland": "#9467bd",
    }
    for region, points in CLIMATE_REGION_POINTS.items():
        lats = [p["lat"] for p in points]
        lons = [p["lon"] for p in points]
        labels = [p["label"] for p in points]
        fig.add_trace(go.Scattergeo(
            lat=lats, lon=lons, text=labels, mode="markers", name=region,
            marker=dict(size=13, color=palette.get(region, "gray"), line=dict(width=1, color="white")),
            hovertext=[f"{region}: {l}" for l in labels], hoverinfo="text",
        ))
    return fig


def link_canals_map() -> go.Figure:
    fig = _base_figure("Link Canals — Indus Basin Irrigation System (IBIS)")
    palette = [
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
        "#8c564b", "#e377c2", "#7f7f7f",
    ]
    for i, (name, pts) in enumerate(LINK_CANAL_LINES.items()):
        lats = [p[0] for p in pts]
        lons = [p[1] for p in pts]
        fig.add_trace(go.Scattergeo(
            lat=lats, lon=lons, mode="lines+markers", name=name,
            line=dict(width=4, color=palette[i % len(palette)], dash="dash"),
            marker=dict(size=7),
            hovertext=name, hoverinfo="text",
        ))
    # overlay the main rivers faintly for geographic context
    for river, points in RIVER_COORDS.items():
        lats = [p[0] for p in points]
        lons = [p[1] for p in points]
        fig.add_trace(go.Scattergeo(
            lat=lats, lon=lons, mode="lines", showlegend=False,
            line=dict(width=1.5, color="rgba(100,150,220,0.5)"), hoverinfo="skip",
        ))
    return fig


def geopolitical_map() -> go.Figure:
    fig = _base_figure("Geo-Political & Strategic Water Infrastructure")
    color_by_type = {
        "Indian upstream project": "#d62728",
        "Pakistan headworks": "#2ca02c",
        "Pakistan hydropower": "#1f77b4",
        "Maritime trade infrastructure": "#9467bd",
        "Regional context": "#7f7f7f",
    }
    by_type = {}
    for name, info in GEOPOLITICAL_COORDS.items():
        by_type.setdefault(info["type"], {"lat": [], "lon": [], "text": []})
        by_type[info["type"]]["lat"].append(info["lat"])
        by_type[info["type"]]["lon"].append(info["lon"])
        by_type[info["type"]]["text"].append(name)
    for t, d in by_type.items():
        fig.add_trace(go.Scattergeo(
            lat=d["lat"], lon=d["lon"], text=d["text"], mode="markers", name=t,
            marker=dict(size=13, color=color_by_type.get(t, "gray"), line=dict(width=1, color="white")),
            hovertext=d["text"], hoverinfo="text",
        ))
    return fig


def india_dam_disputes_map() -> go.Figure:
    fig = _base_figure("India's Upstream Dam Projects — Pakal Dul & Ratle (Chenab Basin)")
    lats = [v["lat"] for v in INDIA_DISPUTED_DAM_COORDS.values()]
    lons = [v["lon"] for v in INDIA_DISPUTED_DAM_COORDS.values()]
    names = [f"{k} — {v['capacity_MW']} MW ({v['river']})" for k, v in INDIA_DISPUTED_DAM_COORDS.items()]
    fig.add_trace(go.Scattergeo(
        lat=lats, lon=lons, text=names, mode="markers+text", name="Disputed upstream dams",
        marker=dict(size=15, color="crimson", symbol="x", line=dict(width=2, color="white")),
        textposition="bottom center", hoverinfo="text",
    ))
    # Show Marala Headworks (Pakistan's downstream receiving point) for context
    fig.add_trace(go.Scattergeo(
        lat=[DAM_COORDS["Marala Headworks"]["lat"]], lon=[DAM_COORDS["Marala Headworks"]["lon"]],
        text=["Marala Headworks (Pakistan, downstream)"], mode="markers+text", name="Downstream (Pakistan)",
        marker=dict(size=13, color="#2ca02c", symbol="triangle-up"), textposition="top center",
        hoverinfo="text",
    ))
    lats_line = [INDIA_DISPUTED_DAM_COORDS["Ratle Dam (India)"]["lat"], DAM_COORDS["Marala Headworks"]["lat"]]
    lons_line = [INDIA_DISPUTED_DAM_COORDS["Ratle Dam (India)"]["lon"], DAM_COORDS["Marala Headworks"]["lon"]]
    fig.add_trace(go.Scattergeo(
        lat=lats_line, lon=lons_line, mode="lines", showlegend=False,
        line=dict(width=2, color="rgba(200,50,50,0.4)", dash="dot"), hoverinfo="skip",
    ))
    return fig


def china_hydropower_map() -> go.Figure:
    fig = _base_figure("CPEC Hydropower Portfolio — China-Financed Projects")
    items = {k: v for k, v in DAM_COORDS.items() if k in CPEC_HYDROPOWER_NAMES}
    lats = [v["lat"] for v in items.values()]
    lons = [v["lon"] for v in items.values()]
    names = [f"{k} ({v['river']}, {v['province']})" for k, v in items.items()]
    fig.add_trace(go.Scattergeo(
        lat=lats, lon=lons, text=names, mode="markers+text", name="CPEC Hydropower Projects",
        marker=dict(size=15, color="#de2910", symbol="star", line=dict(width=1, color="white")),
        textposition="top center", hoverinfo="text",
    ))
    return fig


def historical_events_map() -> go.Figure:
    fig = _base_figure("Historical Disaster Events — Timeline Map")
    lats = [v["lat"] for v in HISTORICAL_EVENT_COORDS.values()]
    lons = [v["lon"] for v in HISTORICAL_EVENT_COORDS.values()]
    names = [f"{k} ({v['year']})" for k, v in HISTORICAL_EVENT_COORDS.items()]
    years = [v["year"] for v in HISTORICAL_EVENT_COORDS.values()]
    fig.add_trace(go.Scattergeo(
        lat=lats, lon=lons, text=names, mode="markers+text", name="Historical Events",
        marker=dict(
            size=16, color=years, colorscale="OrRd", showscale=True,
            colorbar=dict(title="Year"), line=dict(width=1, color="white"),
        ),
        textposition="top center", hoverinfo="text",
    ))
    return fig


def river_confluence_geomap() -> go.Figure:
    """Real-map version: rivers plus labeled confluence points."""
    fig = _base_figure("River Confluence Points (geographic)")
    for river, points in RIVER_COORDS.items():
        lats = [p[0] for p in points]
        lons = [p[1] for p in points]
        fig.add_trace(go.Scattergeo(
            lat=lats, lon=lons, mode="lines", name=river,
            line=dict(width=2.5), hoverinfo="name",
        ))
    conf_lats = [v["lat"] for v in CONFLUENCE_COORDS.values()]
    conf_lons = [v["lon"] for v in CONFLUENCE_COORDS.values()]
    conf_names = list(CONFLUENCE_COORDS.keys())
    fig.add_trace(go.Scattergeo(
        lat=conf_lats, lon=conf_lons, text=conf_names, mode="markers", name="Confluences",
        marker=dict(size=12, color="black", symbol="circle", line=dict(width=1, color="white")),
        hovertext=conf_names, hoverinfo="text",
    ))
    return fig


def irrigation_network_geomap() -> go.Figure:
    """Real-map version: rivers, barrages/dams and link canals together."""
    fig = _base_figure("Irrigation & Hydropower Network (geographic)")
    for river, points in RIVER_COORDS.items():
        lats = [p[0] for p in points]
        lons = [p[1] for p in points]
        fig.add_trace(go.Scattergeo(
            lat=lats, lon=lons, mode="lines", showlegend=False,
            line=dict(width=1.5, color="rgba(31,119,180,0.5)"), hoverinfo="skip",
        ))
    for name, pts in LINK_CANAL_LINES.items():
        lats = [p[0] for p in pts]
        lons = [p[1] for p in pts]
        fig.add_trace(go.Scattergeo(
            lat=lats, lon=lons, mode="lines", name=name,
            line=dict(width=3, color="#ff7f0e", dash="dash"), hoverinfo="name",
        ))
    dam_lats = [v["lat"] for v in DAM_COORDS.values()]
    dam_lons = [v["lon"] for v in DAM_COORDS.values()]
    dam_names = list(DAM_COORDS.keys())
    fig.add_trace(go.Scattergeo(
        lat=dam_lats, lon=dam_lons, text=dam_names, mode="markers", name="Dams / Barrages / Hydropower",
        marker=dict(size=10, color="darkgreen", symbol="triangle-up"), hoverinfo="text",
    ))
    return fig


def custom_points_map(df, title: str = "Uploaded Data on Map") -> go.Figure:
    """
    Build a map from a user-supplied DataFrame with 'Name', 'Latitude' and
    'Longitude' columns (see file_import.py, which produces this shape from
    an uploaded CSV or PDF). Any extra columns are shown in the hover text.
    An optional 'Category' column splits points into separate colored traces.
    The view auto-fits to the plotted points instead of staying pinned to
    Pakistan, since uploaded data may cover any part of the world.
    """
    fig = _base_figure(title)

    hover_cols = [c for c in df.columns if c not in {"Latitude", "Longitude", "Category"}]
    hovertext = df.apply(
        lambda r: "<br>".join(f"{c}: {r[c]}" for c in hover_cols), axis=1
    )

    if "Category" in df.columns:
        palette = [
            "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
            "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
        ]
        for i, (cat, grp) in enumerate(df.groupby("Category")):
            fig.add_trace(go.Scattergeo(
                lat=grp["Latitude"], lon=grp["Longitude"], mode="markers",
                text=hovertext.loc[grp.index], hoverinfo="text", name=str(cat),
                marker=dict(size=11, color=palette[i % len(palette)], line=dict(width=1, color="white")),
            ))
    else:
        fig.add_trace(go.Scattergeo(
            lat=df["Latitude"], lon=df["Longitude"], mode="markers",
            text=hovertext, hoverinfo="text", name="Uploaded points",
            marker=dict(size=12, color="#e6550d", symbol="circle", line=dict(width=1, color="white")),
        ))

    fig.update_geos(fitbounds="locations", visible=True)
    return fig


def forests_map() -> go.Figure:
    fig = _base_figure("Notable Forests of Pakistan")
    lats = [v["lat"] for v in NOTABLE_FOREST_COORDS.values()]
    lons = [v["lon"] for v in NOTABLE_FOREST_COORDS.values()]
    names = [f"{k} ({v['province']})" for k, v in NOTABLE_FOREST_COORDS.items()]
    fig.add_trace(go.Scattergeo(
        lat=lats, lon=lons, text=names, mode="markers+text",
        marker=dict(size=12, color="#2e7d32", symbol="triangle-up", line=dict(width=1, color="white")),
        textposition="top center", name="Notable Forests", hoverinfo="text",
    ))
    return fig


def national_parks_map() -> go.Figure:
    fig = _base_figure("National Parks & Major Recreational Parks of Pakistan")
    lats = [v["lat"] for v in NATIONAL_PARK_COORDS.values()]
    lons = [v["lon"] for v in NATIONAL_PARK_COORDS.values()]
    names = [f"{k} ({v['province']})" for k, v in NATIONAL_PARK_COORDS.items()]
    fig.add_trace(go.Scattergeo(
        lat=lats, lon=lons, text=names, mode="markers",
        marker=dict(size=11, color="#1565c0", symbol="star", line=dict(width=1, color="white")),
        name="Parks", hoverinfo="text",
    ))
    return fig
