"""
network_view.py
Schematic (non-georeferenced) network diagrams of the Indus Basin river,
barrage and link-canal system, built with networkx + plotly so no
extra system dependency (graphviz binary) is required.
"""

import networkx as nx
import plotly.graph_objects as go
from data_loader import RIVERS, DAMS_BARRAGES, LINK_CANALS


def _layout_and_draw(G: nx.DiGraph, title: str, k: float = 0.9) -> go.Figure:
    pos = nx.spring_layout(G, seed=42, k=k, iterations=200)

    edge_x, edge_y = [], []
    for u, v in G.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y, mode="lines",
        line=dict(width=1.5, color="#888"), hoverinfo="none",
    )

    node_x, node_y, node_text, node_color, node_size = [], [], [], [], []
    color_map = {
        "river": "#1f77b4", "barrage": "#2ca02c", "dam": "#d62728",
        "hydropower": "#9467bd", "canal": "#ff7f0e", "confluence": "#17becf",
    }
    for n, attrs in G.nodes(data=True):
        x, y = pos[n]
        node_x.append(x)
        node_y.append(y)
        node_text.append(attrs.get("label", n))
        node_color.append(color_map.get(attrs.get("kind", "river"), "#7f7f7f"))
        node_size.append(attrs.get("size", 22))

    node_trace = go.Scatter(
        x=node_x, y=node_y, mode="markers+text", text=node_text,
        textposition="top center", hoverinfo="text",
        marker=dict(size=node_size, color=node_color, line=dict(width=1, color="white")),
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
        title=title, showlegend=False, height=650,
        margin=dict(l=10, r=10, t=40, b=10),
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        plot_bgcolor="white",
    )
    return fig


def river_confluence_network() -> go.Figure:
    """Rivers as nodes, edges = confluence relationships parsed from RIVERS data."""
    G = nx.DiGraph()
    for river, info in RIVERS.items():
        G.add_node(river, label=river, kind="river", size=26)

    for river, info in RIVERS.items():
        for conf in info.get("confluences", []):
            # extract a plausible target river name if mentioned literally
            for other in RIVERS:
                if other != river and other.split(" River")[0] in conf:
                    G.add_edge(river, other)
    return _layout_and_draw(G, "River Confluence Network (schematic)")


def irrigation_network_diagram() -> go.Figure:
    """Rivers -> barrages/dams -> link canals, schematic flow diagram."""
    G = nx.DiGraph()

    for river in RIVERS:
        G.add_node(river, label=river.replace(" River", ""), kind="river", size=24)

    for name, info in DAMS_BARRAGES.items():
        kind = "dam" if "Dam" in name and "Barrage" not in name else "barrage"
        if "Hydropower" in name:
            kind = "hydropower"
        G.add_node(name, label=name, kind=kind, size=18)
        river = info.get("river")
        if river in RIVERS:
            G.add_edge(river, name)

    for name, info in LINK_CANALS.items():
        G.add_node(name, label=name.split(" (")[0], kind="canal", size=16)
        connects = info.get("connects", "")
        # naive parse: "Indus (Chashma) → Jhelum (Trimmu)"
        parts = connects.split("→")
        if len(parts) == 2:
            src_river = parts[0].strip().split(" (")[0]
            dst_river = parts[1].strip().split(" (")[0]
            for r in RIVERS:
                if r.startswith(src_river):
                    G.add_edge(r, name)
                if r.startswith(dst_river):
                    G.add_edge(name, r)

    return _layout_and_draw(G, "Indus Basin Irrigation Network — Rivers, Barrages/Dams & Link Canals", k=1.1)


def hydropower_cpec_network() -> go.Figure:
    """China-financed hydropower assets mapped to their host rivers."""
    G = nx.DiGraph()
    cpec_projects = {
        "Karot Hydropower Project": "Jhelum River",
        "Suki Kinari Hydropower Station": "Kabul River",
        "Kohala Hydropower Project": "Jhelum River",
        "Azad Pattan Hydropower Project": "Jhelum River",
    }
    for river in set(cpec_projects.values()):
        G.add_node(river, label=river, kind="river", size=26)
    for proj, river in cpec_projects.items():
        G.add_node(proj, label=proj, kind="hydropower", size=20)
        G.add_edge(river, proj)
    return _layout_and_draw(G, "CPEC Hydropower Portfolio by Host River", k=1.3)
