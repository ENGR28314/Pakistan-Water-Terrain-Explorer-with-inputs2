# Pakistan Water, Terrain & Disaster-Risk Explorer

An interactive Streamlit dashboard covering Pakistan's provinces, river
systems, dams/barrages/link canals, climatic regions, mountain ranges,
national disaster-risk context, lakes, and the socio-economic, agro-economic
and geo-political dimensions of water management — including the Indus
Waters Treaty, inter-provincial disputes, CPEC hydropower investment, and
India's upstream dam-design disputes.

## Features

- **Provinces** — Gilgit-Baltistan, KPK, Punjab, Sindh, Balochistan, AJK,
  ICT: capitals, area, rivers, climate, mountain ranges, lakes.
- **Rivers** — source, upstream/downstream path, confluences, associated
  infrastructure, an interactive map, and a schematic confluence network
  diagram.
- **Dams & Barrages** — type, river, province, year completed, capacity,
  purpose, plus a schematic irrigation-network diagram.
- **Link Canals** — the Indus Basin Irrigation System's (IBIS) inter-river
  transfer canals (C-J, T-P, T-S, SMB, MB, R-Q, Q-B, B-S).
- **Climatic Regions** — Temperate, Tropical, Polar, Arid, Highland.
- **Mountain Ranges** — Northern Highlands (Karakoram, Himalayas, Hindu
  Kush, Hindu Raj) and Western/Southern Border Ranges (Spin Ghar, Sulaiman,
  Kirthar, Toba Kakar, Salt Range): highest peaks, surrounding areas,
  climbing details, geology, tourist guides, and associated rivers.
- **Lakes** — major lakes across provinces with formation type.
- **Deserts** — Thar, Cholistan, Kharan, Thal, and the Katpana cold desert,
  with province, approximate area, type, and mapped extents.
- **National Disaster Risk Context** — hazard profile (hydro-meteorological,
  tectonic, climatological/emerging, anthropogenic), exposure & vulnerability
  assessment, emerging risks (GLOFs, erratic monsoons, sea intrusion), and
  baseline / medium / worst-case risk scenarios.
- **Socio-Economic & Agro-Economic Domains** — food security, employment,
  urban growth, tourism, the Indus Basin Irrigation System, GDP linkages.
- **Geo-Political & Strategic Domains** — Kashmir hydro-politics, the Indus
  Waters Treaty, maritime trade infrastructure, Punjab-vs-Sindh internal
  water disputes, and IRSA/CCI/Supreme Court legal mechanisms.
- **China's CPEC Hydropower Footprint** — Karot, Suki Kinari, Kohala, Azad
  Pattan, with a portfolio network diagram.
- **India's Upstream Dam Disputes** — Pakal Dul & Ratle dam technical
  contentions (pondage, freeboard, spillway design) and Court of Arbitration
  interventions.
- **Interactive Hydraulic Models** — simplified reservoir mass-balance
  simulation, shortage-sharing allocation, link-canal transfer calculator,
  and a composite disaster-risk-index tool.
- **Upload File → Map** — upload your own **CSV or PDF** of location data and
  the app plots it on an interactive map. CSVs need recognizable
  latitude/longitude columns (`lat`/`lon`, `latitude`/`longitude`, etc.), with
  optional `name` and `category` columns; PDFs work either as a table with
  the same kind of columns, or as plain text containing coordinate pairs
  (e.g. `Site A: 31.52, 74.35`).

## Project structure

```
.
├── app.py                # Main Streamlit application (page/section routing)
├── data_loader.py         # All curated reference data (provinces, rivers, dams,
│                           # canals, climate, mountains, disaster risk, lakes,
│                           # socio-economic, geo-political, CPEC, India disputes)
├── coordinates.py         # Lat/lon reference data used for mapping
├── map_view.py             # Plotly geographic map builders
├── network_view.py         # NetworkX + Plotly schematic network diagrams
├── hydraulic_model.py       # Simplified interactive hydraulic/risk models
├── file_import.py           # CSV/PDF → lat/lon DataFrame parsing (Upload File → Map tab)
├── requirements.txt
├── .gitignore
└── README.md
```

## Running locally

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## Data accuracy & scope note

This is an **educational/reference dashboard**. Coordinates are
approximate, and infrastructure figures (capacities, completion years,
allocation percentages) are curated summaries for visualization purposes.
Before using any figure in a formal, legal or engineering context, verify
against primary sources: WAPDA, IRSA, PMD, NDMA/PDMA, the Indus Waters
Treaty (1960) text, and the Water Apportionment Accord (1991). The
interactive hydraulic and risk-index models in the final tab are simplified
teaching tools, not validated simulators.

## Notes on compiled files

Compiled bytecode files (`.cpython-*.pyc`, under `__pycache__/`) are
generated automatically by Python when the app runs — they are not meant
to be hand-authored or committed, which is why `.gitignore` excludes them.
