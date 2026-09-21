"""
data_loader.py
Central data module for the Pakistan Water & Geography Explorer Streamlit app.
All data is curated/summarized for an educational dashboard. Figures such as
capacities, elevations and discharge should be verified against primary
sources (WAPDA, IRSA, PMD, PDMA/NDMA) before use in any formal report.
"""

# ---------------------------------------------------------------------------
# 1. PROVINCES
# ---------------------------------------------------------------------------
PROVINCES = {
    "Gilgit-Baltistan": {
        "capital": "Gilgit",
        "area_km2": 72971,
        "overview": (
            "Mountainous northern territory containing the confluence of the "
            "Karakoram, Himalaya and Hindu Kush ranges. Home to K2 and the "
            "headwaters of the Indus, Gilgit, Hunza and Shyok rivers."
        ),
        "major_rivers": ["Indus River", "Gilgit River", "Hunza River", "Shyok River"],
        "major_dams_barrages": ["Diamer-Bhasha Dam (under construction)"],
        "climate_regions": ["Highland", "Arid (valley floors)"],
        "mountain_ranges": ["Karakoram Range", "Himalayas Range (western edge)", "Hindu Kush Range"],
        "key_lakes": ["Attabad Lake", "Satpara Lake", "Rush Lake", "Ghizer Lake"],
    },
    "Khyber Pakhtunkhwa (KPK)": {
        "capital": "Peshawar",
        "area_km2": 101741,
        "overview": (
            "Bridges the northern highlands and the Indus plains. Drained by "
            "the Kabul and Swat rivers before they join the Indus near "
            "Attock; contains Tarbela Dam, the country's largest earth-filled dam."
        ),
        "major_rivers": ["Kabul River", "Swat River", "Indus River"],
        "major_dams_barrages": ["Tarbela Dam", "Warsak Dam", "Suki Kinari Hydropower Station"],
        "climate_regions": ["Highland (north)", "Temperate", "Arid (south)"],
        "mountain_ranges": ["Hindu Kush Range", "Hindu Raj Range", "Spin Ghar (Koh-e-Safed)"],
        "key_lakes": ["Saif-ul-Malook Lake"],
    },
    "Punjab": {
        "capital": "Lahore",
        "area_km2": 205344,
        "overview": (
            "The agricultural heartland fed by the five rivers of the "
            "Indus Basin Irrigation System (IBIS) — Indus, Jhelum, Chenab, "
            "Ravi and Sutlej — linked by an extensive canal and barrage network."
        ),
        "major_rivers": ["Indus River", "Jhelum River", "Chenab River", "Ravi River", "Sutlej River"],
        "major_dams_barrages": [
            "Mangla Dam (partly AJK)", "Chashma Barrage", "Taunsa Barrage",
            "Trimmu Barrage", "Rasul Barrage", "Panjnad Barrage", "Marala Headworks",
        ],
        "climate_regions": ["Arid", "Semi-arid/Temperate (north)"],
        "mountain_ranges": ["Salt Range"],
        "key_lakes": [],
    },
    "Sindh": {
        "capital": "Karachi",
        "area_km2": 140914,
        "overview": (
            "Lower riparian province where the Indus terminates in a delta on "
            "the Arabian Sea. Heavily dependent on Sukkur, Guddu and Kotri "
            "barrages; most exposed to sea intrusion and coastal salinization."
        ),
        "major_rivers": ["Indus River"],
        "major_dams_barrages": ["Guddu Barrage", "Sukkur Barrage", "Kotri Barrage"],
        "climate_regions": ["Arid", "Tropical (coastal belt)"],
        "mountain_ranges": ["Kirthar Range"],
        "key_lakes": ["Manchar Lake", "Keenjhar Lake", "Hub Dam Lake"],
    },
    "Balochistan": {
        "capital": "Quetta",
        "area_km2": 347190,
        "overview": (
            "Largest and most arid province, drained mostly by seasonal "
            "hill-torrent systems (Zhob, Bolan, Hingol, Dasht) rather than "
            "perennial rivers. Highly exposed to flash floods and drought."
        ),
        "major_rivers": ["Zhob River", "Bolan River", "Hingol River", "Dasht River"],
        "major_dams_barrages": ["Hub Dam", "Mirani Dam", "Sabakzai Dam"],
        "climate_regions": ["Arid", "Highland (Quetta plateau)"],
        "mountain_ranges": ["Toba Kakar Range", "Sulaiman Mountains (Koh-e-Suleman)", "Kirthar Range (east)"],
        "key_lakes": ["Hanna Lake"],
    },
    "Azad Jammu & Kashmir (AJK)": {
        "capital": "Muzaffarabad",
        "area_km2": 13297,
        "overview": (
            "Mountainous territory straddling the Jhelum River, downstream of "
            "Indian-administered projects on the Chenab/Jhelum tributaries; "
            "site of Mangla Dam and several run-of-river hydropower projects."
        ),
        "major_rivers": ["Jhelum River", "Neelum River", "Poonch River"],
        "major_dams_barrages": ["Mangla Dam", "Kohala Hydropower Project", "Azad Pattan Hydropower Project", "Karot Hydropower Project"],
        "climate_regions": ["Highland", "Temperate"],
        "mountain_ranges": ["Himalayas Range (Pir Panjal foothills)"],
        "key_lakes": ["Banjosa Lake"],
    },
    "Islamabad Capital Territory (ICT)": {
        "capital": "Islamabad",
        "area_km2": 906,
        "overview": (
            "Federal capital territory at the foot of the Margalla Hills, "
            "fed by the Soan River and Rawal/Khanpur reservoirs for domestic water supply."
        ),
        "major_rivers": ["Soan River"],
        "major_dams_barrages": ["Rawal Dam", "Khanpur Dam (KPK border)"],
        "climate_regions": ["Temperate"],
        "mountain_ranges": ["Margalla Hills (Himalayan foothills)"],
        "key_lakes": ["Khanpur Lake"],
    },
}

# ---------------------------------------------------------------------------
# 2. RIVERS
# ---------------------------------------------------------------------------
RIVERS = {
    "Indus River": {
        "length_km": 3180,
        "source": "Tibetan Plateau, near Lake Mansarovar / Senge Khabab (enters Pakistan through GB)",
        "upstream": "Enters Pakistan in Gilgit-Baltistan (Ladakh border) flowing through the Karakoram gorges.",
        "downstream": "Flows through KPK, Punjab and Sindh to the Indus Delta, Arabian Sea near Karachi/Thatta.",
        "confluences": [
            "Kabul River (near Attock, KPK)",
            "Panjnad River — combined Jhelum/Chenab/Ravi/Sutlej (near Mithankot, Punjab)",
            "Gilgit & Hunza rivers (near Bunji, GB)",
        ],
        "provinces": ["Gilgit-Baltistan", "KPK", "Punjab", "Sindh"],
        "dams_barrages": ["Tarbela Dam", "Chashma Barrage", "Taunsa Barrage", "Guddu Barrage", "Sukkur Barrage", "Kotri Barrage", "Diamer-Bhasha Dam (under construction)"],
    },
    "Jhelum River": {
        "length_km": 725,
        "source": "Verinag Spring, Indian-administered Kashmir",
        "upstream": "Enters AJK near Muzaffarabad after flowing through the Kashmir Valley.",
        "downstream": "Joins the Chenab River near Trimmu, Punjab.",
        "confluences": ["Neelum River (Muzaffarabad)", "Chenab River (Trimmu, Punjab)"],
        "provinces": ["AJK", "KPK", "Punjab"],
        "dams_barrages": ["Mangla Dam", "Rasul Barrage", "Trimmu Barrage", "Kohala & Azad Pattan hydropower (run-of-river)"],
    },
    "Chenab River": {
        "length_km": 960,
        "source": "Himachal Pradesh, India (Chandra & Bhaga rivers)",
        "upstream": "Enters Punjab at Marala, near Sialkot.",
        "downstream": "Joins the Sutlej/Panjnad system near Uch Sharif, Punjab.",
        "confluences": ["Jhelum River (Trimmu)", "Ravi River (Ahmadpur Sial)", "Sutlej (forming Panjnad)"],
        "provinces": ["Punjab"],
        "dams_barrages": ["Marala Headworks", "Trimmu Barrage"],
        "notes": "Focus of India–Pakistan hydro-political disputes (Baglihar, Pakal Dul, Ratle projects upstream).",
    },
    "Ravi River": {
        "length_km": 720,
        "source": "Himachal Pradesh, India",
        "upstream": "Enters Punjab near Shahdara, Lahore.",
        "downstream": "Joins the Chenab River near Ahmadpur Sial.",
        "confluences": ["Chenab River"],
        "provinces": ["Punjab"],
        "dams_barrages": ["Balloki Headworks", "Sidhnai Barrage"],
    },
    "Sutlej River": {
        "length_km": 1450,
        "source": "Rakshastal Lake, Tibet",
        "upstream": "Enters Punjab near Sulemanki after flowing through Indian Punjab (largely dry in Pakistan post-Indus Waters Treaty apportionment).",
        "downstream": "Joins the Panjnad/Chenab system near Bahawalpur.",
        "confluences": ["Panjnad River"],
        "provinces": ["Punjab"],
        "dams_barrages": ["Sulemanki Headworks", "Islam Headworks", "Panjnad Barrage"],
        "notes": "Allocated to India under the 1960 Indus Waters Treaty; flow in Pakistan is seasonal/residual.",
    },
    "Kabul River": {
        "length_km": 700,
        "source": "Sanglakh Range, Afghanistan (near Kabul)",
        "upstream": "Enters KPK near Torkham/Warsak.",
        "downstream": "Joins the Indus River near Attock.",
        "confluences": ["Swat River (Charsadda)", "Indus River (Attock)"],
        "provinces": ["KPK"],
        "dams_barrages": ["Warsak Dam"],
    },
    "Swat River": {
        "length_km": 240,
        "source": "Hindu Kush foothills, upper Swat valley",
        "upstream": "Flows south through Kalam, Mingora.",
        "downstream": "Joins the Kabul River near Charsadda.",
        "confluences": ["Kabul River"],
        "provinces": ["KPK"],
        "dams_barrages": ["Munda Dam (planned/under development)"],
    },
    "Gilgit River": {
        "length_km": 240,
        "source": "Shandur Pass area, GB",
        "upstream": "Flows through Ghizer and Gilgit valleys.",
        "downstream": "Joins the Indus River near Bunji.",
        "confluences": ["Hunza River (near Gilgit town)", "Indus River (Bunji)"],
        "provinces": ["Gilgit-Baltistan"],
        "dams_barrages": [],
    },
    "Hunza River": {
        "length_km": 190,
        "source": "Glaciers of the Karakoram (Batura, Hispar)",
        "upstream": "Flows through Hunza and Nagar valleys.",
        "downstream": "Joins the Gilgit River near Gilgit town.",
        "confluences": ["Gilgit River"],
        "provinces": ["Gilgit-Baltistan"],
        "dams_barrages": [],
        "notes": "Site of the 2010 Attabad Lake landslide-dam disaster.",
    },
    "Zhob River": {
        "length_km": 320,
        "source": "Toba Kakar Range, Balochistan",
        "upstream": "Flows through Zhob district.",
        "downstream": "Joins the Gomal River, then the Indus in southern KPK/Punjab border.",
        "confluences": ["Gomal River"],
        "provinces": ["Balochistan"],
        "dams_barrages": ["Sabakzai Dam"],
    },
    "Bolan River": {
        "length_km": 200,
        "source": "Central Brahui Range, Balochistan",
        "upstream": "Flows through the Bolan Pass.",
        "downstream": "Dissipates into the Kachhi plain (seasonal hill torrent).",
        "confluences": ["Terminal/inland — does not reach the sea"],
        "provinces": ["Balochistan"],
        "dams_barrages": ["Bolan Dam"],
    },
    "Hingol River": {
        "length_km": 560,
        "source": "Central Balochistan highlands",
        "upstream": "Flows through Hingol National Park.",
        "downstream": "Empties into the Arabian Sea at Hingol delta.",
        "confluences": ["Arabian Sea outfall"],
        "provinces": ["Balochistan"],
        "dams_barrages": [],
    },
    "Dasht River": {
        "length_km": 400,
        "source": "Central Makran highlands, Balochistan",
        "upstream": "Flows through Kech/Turbat.",
        "downstream": "Empties into the Arabian Sea near Gwadar.",
        "confluences": ["Nihing River"],
        "provinces": ["Balochistan"],
        "dams_barrages": ["Mirani Dam"],
    },
}

# ---------------------------------------------------------------------------
# 3. DAMS & BARRAGES (detail table)
# ---------------------------------------------------------------------------
DAMS_BARRAGES = {
    "Tarbela Dam": {"type": "Earth-filled dam", "river": "Indus River", "province": "KPK",
                    "year_completed": 1976, "capacity_MW": 4888, "purpose": "Irrigation storage & hydropower"},
    "Mangla Dam": {"type": "Embankment dam", "river": "Jhelum River", "province": "AJK/Punjab",
                   "year_completed": 1967, "capacity_MW": 1310, "purpose": "Irrigation storage & hydropower"},
    "Diamer-Bhasha Dam": {"type": "Concrete-face rock-fill dam (under construction)", "river": "Indus River",
                          "province": "GB/KPK border", "year_completed": "2029-31 (planned)",
                          "capacity_MW": 4500, "purpose": "Irrigation storage, hydropower & flood control"},
    "Warsak Dam": {"type": "Gravity dam", "river": "Kabul River", "province": "KPK",
                   "year_completed": 1960, "capacity_MW": 243, "purpose": "Hydropower & irrigation"},
    "Chashma Barrage": {"type": "Barrage", "river": "Indus River", "province": "Punjab",
                        "year_completed": 1971, "capacity_MW": None, "purpose": "Irrigation diversion"},
    "Taunsa Barrage": {"type": "Barrage", "river": "Indus River", "province": "Punjab",
                       "year_completed": 1958, "capacity_MW": None, "purpose": "Irrigation diversion"},
    "Guddu Barrage": {"type": "Barrage", "river": "Indus River", "province": "Sindh",
                      "year_completed": 1962, "capacity_MW": None, "purpose": "Irrigation diversion"},
    "Sukkur Barrage": {"type": "Barrage", "river": "Indus River", "province": "Sindh",
                       "year_completed": 1932, "capacity_MW": None, "purpose": "Irrigation diversion (world's largest irrigation network anchor)"},
    "Kotri Barrage": {"type": "Barrage", "river": "Indus River", "province": "Sindh",
                      "year_completed": 1955, "capacity_MW": None, "purpose": "Irrigation diversion & downstream/delta flow releases"},
    "Karot Hydropower Project": {"type": "Run-of-river hydropower (CPEC)", "river": "Jhelum River",
                                  "province": "Punjab/AJK", "year_completed": 2022, "capacity_MW": 720,
                                  "purpose": "Hydropower — Chinese IPP investment"},
    "Suki Kinari Hydropower Station": {"type": "Run-of-river hydropower (CPEC)", "river": "Kunhar River",
                                        "province": "KPK", "year_completed": 2024, "capacity_MW": 884,
                                        "purpose": "Hydropower — Chinese IPP investment"},
    "Kohala Hydropower Project": {"type": "Run-of-river hydropower (CPEC, under development)", "river": "Jhelum River",
                                   "province": "KPK/AJK", "year_completed": "2026-27 (planned)", "capacity_MW": 1124,
                                   "purpose": "Hydropower — Chinese IPP investment"},
    "Azad Pattan Hydropower Project": {"type": "Run-of-river hydropower (CPEC, under development)", "river": "Jhelum River",
                                        "province": "AJK", "year_completed": "2027 (planned)", "capacity_MW": 700.7,
                                        "purpose": "Hydropower — Chinese IPP investment"},
}

# ---------------------------------------------------------------------------
# 4. LINK CANALS (Indus Basin Irrigation System)
# ---------------------------------------------------------------------------
LINK_CANALS = {
    "Chashma-Jhelum (C-J) Link Canal": {"connects": "Indus (Chashma) → Jhelum (Trimmu)", "province": "Punjab",
                                         "purpose": "Transfers surplus Indus water to the Jhelum/Chenab system to compensate Ravi/Sutlej users after IWT."},
    "Taunsa-Panjnad (T-P) Link Canal": {"connects": "Indus (Taunsa) → Panjnad", "province": "Punjab",
                                         "purpose": "Supplements Sutlej-zone irrigation supplies."},
    "Trimmu-Sidhnai (T-S) Link Canal": {"connects": "Chenab (Trimmu) → Ravi (Sidhnai)", "province": "Punjab",
                                         "purpose": "Feeds central Punjab (Ravi zone) canal commands."},
    "Sidhnai-Mailsi-Bahawal (SMB) Link Canal": {"connects": "Ravi (Sidhnai) → Sutlej (Bahawal)", "province": "Punjab",
                                                 "purpose": "Extends Ravi water into the Sutlej command area."},
    "Mailsi-Bahawal (MB) Link Canal": {"connects": "Continuation of SMB system", "province": "Punjab",
                                        "purpose": "Feeds Bahawalpur-zone irrigation."},
    "Rasul-Qadirabad (R-Q) Link Canal": {"connects": "Jhelum (Rasul) → Chenab (Qadirabad)", "province": "Punjab",
                                          "purpose": "Balances Jhelum surplus into the Chenab system."},
    "Qadirabad-Balloki (Q-B) Link Canal": {"connects": "Chenab (Qadirabad) → Ravi (Balloki)", "province": "Punjab",
                                            "purpose": "Feeds the Ravi command after the river's flows were reduced post-IWT."},
    "Balloki-Sulemanki (B-S) Link Canal": {"connects": "Ravi (Balloki) → Sutlej (Sulemanki)", "province": "Punjab",
                                            "purpose": "Reinforces the Sutlej zone with Ravi/Chenab water."},
}

# ---------------------------------------------------------------------------
# 5. CLIMATIC REGIONS
# ---------------------------------------------------------------------------
CLIMATIC_REGIONS = {
    "Temperate": {
        "areas": ["Northern KPK valleys", "Islamabad/Margalla foothills", "AJK mid-elevations"],
        "characteristics": "Four distinct seasons, moderate rainfall, monsoon influence in summer, cold winters with occasional snow at higher elevations.",
    },
    "Tropical": {
        "areas": ["Coastal Sindh/Karachi belt"],
        "characteristics": "Warm and humid year-round, moderated by the Arabian Sea, monsoon-dependent rainfall, vulnerable to cyclones and sea intrusion.",
    },
    "Polar": {
        "areas": ["High-altitude Karakoram/Himalaya glaciated zones above ~5000 m"],
        "characteristics": "Permanent snow and ice cover, extreme cold, the source zone for glacier-fed rivers and the location of most GLOF hazard.",
    },
    "Arid": {
        "areas": ["Most of Balochistan", "Southern Punjab", "Sindh interior", "Thar Desert"],
        "characteristics": "Very low and erratic rainfall, high evapotranspiration, heavy reliance on irrigation, drought-prone.",
    },
    "Highland": {
        "areas": ["Gilgit-Baltistan valleys", "Quetta plateau", "Northern KPK mountains"],
        "characteristics": "Cold semi-arid to alpine conditions, large diurnal temperature range, snowmelt-dependent hydrology.",
    },
}

# ---------------------------------------------------------------------------
# 6. MOUNTAIN RANGES
# ---------------------------------------------------------------------------
MOUNTAIN_RANGES = {
    "Northern Highlands and Major Ranges": {
        "Karakoram Range": {
            "highest_peak": "K2 (Mount Godwin-Austen), 8,611 m — 2nd highest peak on Earth",
            "other_notable_peaks": [
                {"name": "Gasherbrum I (Hidden Peak)", "elevation_m": 8080},
                {"name": "Broad Peak", "elevation_m": 8051},
                {"name": "Gasherbrum II", "elevation_m": 8035},
                {"name": "Masherbrum", "elevation_m": 7821},
                {"name": "Rakaposhi", "elevation_m": 7788},
                {"name": "Batura Sar", "elevation_m": 7795},
            ],
            "surrounding_areas": "Gilgit-Baltistan (Baltistan, Hunza, Shigar, Skardu)",
            "climbing_details": (
                "K2 is climbed mainly via the Abruzzi Spur (Southeast Ridge) from Concordia, "
                "reached by a multi-day trek up the Baltoro Glacier; the Cesen and North Ridge "
                "routes are used less often. K2 is considered far more technical and dangerous "
                "than Everest — steep ice and rock climbing, frequent avalanches on the "
                "'Bottleneck' serac traverse near the summit, and a historically high "
                "fatality-to-summit ratio have earned it the nickname 'Savage Mountain'. "
                "It was first summited in 1954 by an Italian expedition (Lino Lacedelli and "
                "Achille Compagnoni) and was first climbed in winter only in January 2021, by a "
                "Nepali team."
            ),
            "best_climbing_season": "Late June to August (summer expedition window); winter ascents attempted rarely, Dec-Feb.",
            "permits_required": "Mountaineering/trekking permit from the Gilgit-Baltistan tourism authorities and Pakistan's Alpine Club; peak fee scaled to expedition size for 8,000 m peaks.",
            "access_towns": ["Skardu", "Askole (last road-head village)"],
            "trekking_routes": ["Askole → Baltoro Glacier → Concordia → K2 Base Camp", "Concordia → Gondogoro La → Hushe valley"],
            "hazards": "Serac/avalanche fall on upper routes, sudden weather changes, rockfall in the Baltoro approach, altitude illness.",
            "geology": "Young, tectonically active granite/gneiss massif formed by the ongoing India-Asia collision; one of the most heavily glaciated areas outside the polar regions, often called the 'Third Pole' — the Baltoro and Biafo glaciers are among the longest outside the poles.",
            "tourist_guide": (
                "The Baltoro Glacier trek to Concordia (the 'throne room of the mountain gods', "
                "ringed by four of the world's 8,000 m peaks) is one of the most spectacular "
                "trekking routes on Earth. Nearby highlights include the granite spires of the "
                "Trango Towers (a world-class big-wall climbing destination), the alpine Deosai "
                "Plateau (accessed via Skardu, home to the Himalayan brown bear), and Shigar Fort "
                "for cultural heritage."
            ),
            "rivers": ["Indus River (headwaters)", "Shyok River", "Hunza River", "Shigar River"],
        },
        "Himalayas Range": {
            "highest_peak": "Nanga Parbat, 8,126 m — westernmost 8000er, 9th highest in the world",
            "other_notable_peaks": [
                {"name": "Rakhiot Peak", "elevation_m": 7070},
                {"name": "Laila Peak (Gasherbrum group)", "elevation_m": 6096},
                {"name": "Malika Parbat", "elevation_m": 5290},
            ],
            "surrounding_areas": "Gilgit-Baltistan (Diamer district), AJK, extending east into Indian-administered Kashmir and northern India",
            "climbing_details": (
                "Nanga Parbat, nicknamed 'Killer Mountain' after a string of early-20th-century "
                "fatalities (notably the 1934 and 1937 German expeditions), is typically climbed "
                "via the Kinshofer route on the Diamir Face; the Rupal Face on the southern side "
                "is one of the tallest mountain faces in the world (~4,600 m of relief). First "
                "summited in 1953 by Hermann Buhl, solo on the final push."
            ),
            "best_climbing_season": "June to August for the standard season; a small number of winter ascents have succeeded since 2016.",
            "permits_required": "Mountaineering permit from the Gilgit-Baltistan tourism department / Alpine Club of Pakistan.",
            "access_towns": ["Chilas", "Raikot Bridge (road-head for Fairy Meadows)"],
            "trekking_routes": ["Raikot Bridge → Fairy Meadows → Nanga Parbat Base Camp", "Rupal valley trek to the Rupal Face"],
            "hazards": "Rockfall and avalanche on the Diamir Face, extreme relief on the Rupal Face, rapid weather deterioration.",
            "geology": "One of the fastest-uplifting massifs on Earth, sitting at the western syntaxis where the Himalayan collision zone bends sharply northward around the Indus gorge — a site of intense erosion-uplift feedback studied globally by geologists.",
            "tourist_guide": (
                "Fairy Meadows, a lush alpine meadow with a classic postcard view of Nanga "
                "Parbat's Diamir Face, is reachable by jeep and a short trek from Raikot Bridge "
                "and is one of Pakistan's most-visited mountain viewpoints. The Astor valley "
                "offers further trekking and traditional villages."
            ),
            "rivers": ["Indus River", "Jhelum River (headwaters area)", "Neelum River"],
        },
        "Hindu Kush Range": {
            "highest_peak": "Tirich Mir, 7,708 m — highest peak of the Hindu Kush",
            "other_notable_peaks": [
                {"name": "Noshaq (mostly in Afghanistan, visible from Chitral)", "elevation_m": 7492},
                {"name": "Istor-o-Nal", "elevation_m": 7403},
                {"name": "Saraghrar", "elevation_m": 7349},
            ],
            "surrounding_areas": "Chitral district, KPK, bordering Afghanistan's Wakhan Corridor and Nuristan/Badakhshan",
            "climbing_details": (
                "Tirich Mir was first climbed in 1950 by a Norwegian expedition (Arne Naess); "
                "routes are approached via the Tirich Gol valley from Chitral town. Less "
                "commercially guided than the Karakoram 8,000ers, drawing smaller expeditions."
            ),
            "best_climbing_season": "July to early September.",
            "permits_required": "Mountaineering permit via the Alpine Club of Pakistan; border-zone travel permits for areas near Afghanistan.",
            "access_towns": ["Chitral town", "Shagrom (Tirich Gol trailhead)"],
            "trekking_routes": ["Chitral → Tirich Gol valley → Tirich Mir base camp", "Chitral → Kalash valleys circuit"],
            "hazards": "Remote/limited rescue infrastructure, border-proximity access restrictions, glacier crevasses.",
            "geology": "A complex fold-and-thrust belt formed by the oblique collision of the Indian Plate margin with the Eurasian plate along the Afghan border zone; seismically very active, with frequent moderate earthquakes centered in the Hindu Kush.",
            "tourist_guide": (
                "The Chitral valley and the culturally distinct Kalash valleys (Bumburet, Rumbur, "
                "Birir), home to the indigenous Kalash people and their unique festivals, are the "
                "region's signature attractions. The Shandur Pass hosts the famous high-altitude "
                "polo festival each July, at roughly 3,700 m."
            ),
            "rivers": ["Kabul River (tributaries)", "Chitral/Kunar River"],
        },
        "Hindu Raj Range": {
            "highest_peak": "Koh-e-Bandaka, 6,812 m",
            "other_notable_peaks": [
                {"name": "Buni Zom", "elevation_m": 6551},
                {"name": "Thui I", "elevation_m": 6524},
            ],
            "surrounding_areas": "Gilgit-Baltistan/Chitral border zone, wedged between the Hindu Kush and Karakoram ranges",
            "climbing_details": "One of the least explored ranges in the region; several peaks remain unclimbed or only rarely summited, making it attractive for exploratory/first-ascent expeditions.",
            "best_climbing_season": "July to August, weather-dependent.",
            "permits_required": "Mountaineering permit via the Alpine Club of Pakistan; some zones require special/restricted-area permits.",
            "access_towns": ["Gilgit", "Mastuj (Chitral side)"],
            "trekking_routes": ["Yasin valley → Darkot Pass → Chitral (classic trans-range trek)", "Ishkoman valley treks"],
            "hazards": "Very limited rescue/communications infrastructure, glacier travel, unpredictable weather.",
            "geology": "A transitional metamorphic range linking the Hindu Kush and Karakoram tectonic domains, with less well-documented geology than its higher-profile neighbors.",
            "tourist_guide": "Yasin and Ishkoman valleys offer quieter, less-visited trekking corridors connecting Chitral and Gilgit, popular with more experienced trekkers seeking solitude.",
            "rivers": ["Gilgit River (tributaries)", "Yasin River"],
        },
    },
    "Western and Southern Border Ranges": {
        "Spin Ghar (Koh-e-Safed)": {
            "highest_peak": "Sikaram, 4,761 m",
            "other_notable_peaks": [
                {"name": "Mila Sikaram (secondary summit)", "elevation_m": 4712},
            ],
            "surrounding_areas": "Kurram district, KPK, straddling the Pakistan-Afghanistan border (the name means 'White Mountain' for its winter snow cap)",
            "climbing_details": "A moderate-altitude range with straightforward trekking rather than technical mountaineering; access has historically been limited by security conditions along the border, so organized expeditions are uncommon.",
            "best_climbing_season": "May to September, when high routes are snow-free.",
            "permits_required": "Local security clearance/NOC typically required for the Kurram border zone.",
            "access_towns": ["Parachinar"],
            "trekking_routes": ["Parachinar → Sikaram approach (security permitting)"],
            "hazards": "Access/security restrictions, landmines/unexploded ordnance legacy in some border areas, cold exposure.",
            "geology": "A limestone-dominated folded range, part of the western fold belt bordering the Iranian plateau, geologically continuous with ranges extending into eastern Afghanistan.",
            "tourist_guide": "The Kurram valley and the Parachinar area (access-restricted at times) offer highland scenery and are historically significant Silk Road transit corridors.",
            "rivers": ["Kurram River"],
        },
        "Sulaiman Mountains (Koh-e-Suleman)": {
            "highest_peak": "Takht-e-Sulaiman, 3,487 m",
            "other_notable_peaks": [
                {"name": "Kaisargarh (Sulaiman range secondary peak)", "elevation_m": 3383},
            ],
            "surrounding_areas": "Border zone of Balochistan, KPK (Dera Ismail Khan) and Punjab (Dera Ghazi Khan)",
            "climbing_details": "Accessible via Zhob or Fort Munro; a culturally and religiously significant peak, with a shrine near the summit associated with local legend, making it as much a pilgrimage trek as a mountaineering objective.",
            "best_climbing_season": "March to May and September to November (avoiding extreme summer heat at lower elevations).",
            "permits_required": "Local district permission recommended; some routes cross tribal-administered land requiring coordination with local authorities.",
            "access_towns": ["Fort Munro", "Zhob"],
            "trekking_routes": ["Fort Munro → Takht-e-Sulaiman summit trek"],
            "hazards": "Extreme heat at lower elevations outside winter, limited water sources en route, rugged unmarked trails.",
            "geology": "A folded sedimentary range formed by the collision of the Indian Plate with the Afghan block, marking the western structural edge of the Indus plains and a transition zone between the Iranian plateau and the subcontinent.",
            "tourist_guide": "Fort Munro is a small hill station popular for its cooler climate relative to the surrounding plains; the Zhob valley offers additional highland scenery and access to the range's northern flank.",
            "rivers": ["Zhob River", "Gomal River", "Sanghar River"],
        },
        "Kirthar Range": {
            "highest_peak": "Zardak, 2,168 m",
            "other_notable_peaks": [
                {"name": "Kutte-ji-Qabar", "elevation_m": 2050},
            ],
            "surrounding_areas": "Border of Sindh and Balochistan, largely within Kirthar National Park",
            "climbing_details": "A low-technical trekking range rather than a mountaineering destination; Kirthar National Park is the main access and management point, with guided day hikes and short treks.",
            "best_climbing_season": "November to March (avoiding the extreme summer heat of the lower Sindh/Balochistan border zone).",
            "permits_required": "Sindh Wildlife Department entry permit for Kirthar National Park.",
            "access_towns": ["Karachi (gateway city)", "Karchat"],
            "trekking_routes": ["Karchat → Kirthar plateau day treks", "Wildlife-viewing drives through the National Park"],
            "hazards": "Extreme summer heat, scarce water sources, remote terrain with limited cell coverage.",
            "geology": "A folded limestone range, part of the outer fold belt bordering the lower Indus plain, with fossil-rich sedimentary layers of interest to regional geologists.",
            "tourist_guide": "Kirthar National Park protects Sindh ibex and urial habitat and is one of the largest protected areas in Pakistan; the range's dramatic layered limestone cliffs are a draw for photographers.",
            "rivers": ["Hab River", "Western Nara (seasonal drainages)"],
        },
        "Toba Kakar Range": {
            "highest_peak": "Khalifat Peak, ~3,487 m",
            "other_notable_peaks": [
                {"name": "Zarghun Ghar", "elevation_m": 3578},
            ],
            "surrounding_areas": "Pishin and Qila Abdullah districts, Balochistan, near the Afghan border (Chaman crossing)",
            "climbing_details": "Rugged, arid terrain with limited formal climbing infrastructure; most ascents are informal/local rather than organized expeditions.",
            "best_climbing_season": "April to June and September to October.",
            "permits_required": "Local security coordination recommended given proximity to the Afghan border.",
            "access_towns": ["Quetta", "Ziarat"],
            "trekking_routes": ["Ziarat → Khalifat Peak approach", "Quetta plateau day hikes"],
            "hazards": "Border-zone security considerations, arid terrain with limited water, extreme temperature swings.",
            "geology": "A folded and faulted range at the tectonic boundary of the Afghan and Indian blocks, part of the broader Baluchistan fold belt shaped by oblique plate convergence.",
            "tourist_guide": "The Ziarat juniper forests (among the oldest juniper stands in the world) and the cool Quetta plateau climate make this range a popular summer retreat for residents of the surrounding lowlands.",
            "rivers": ["Zhob River (headwaters)", "Pishin Lora River"],
        },
        "Salt Range": {
            "highest_peak": "Sakesar, 1,522 m",
            "other_notable_peaks": [
                {"name": "Chail (Salt Range escarpment high point)", "elevation_m": 1030},
            ],
            "surrounding_areas": "Northern Punjab (Khushab, Chakwal, Jhelum districts), overlooking the Potohar Plateau",
            "climbing_details": "A low hill range suited to hiking and day trips rather than mountaineering; scenic escarpment drives and short trails are the norm.",
            "best_climbing_season": "October to March (summer is very hot at these lower elevations).",
            "permits_required": "None for general tourist access; mine visits (Khewra) are ticketed.",
            "access_towns": ["Khewra", "Kallar Kahar", "Chakwal"],
            "trekking_routes": ["Katas Raj → Salt Range escarpment viewpoint walks"],
            "hazards": "Extreme summer heat, otherwise a low-risk range for casual visitors.",
            "geology": (
                "World-famous for the Khewra Salt Mine (one of the largest salt deposits on "
                "Earth) and a rich Precambrian-to-Eocene sedimentary sequence exposed along its "
                "escarpments; the range is a key stratigraphic reference section used globally in "
                "South Asian geology, including a well-studied Permian-Triassic boundary sequence."
            ),
            "tourist_guide": "The Khewra Salt Mine (including its illuminated salt-crystal chambers), the ancient Hindu Katas Raj Temples complex, and Kallar Kahar's seasonal lake are the range's principal tourist draws, all within easy reach of Islamabad/Lahore.",
            "rivers": ["Soan River (adjacent)"],
        },
    },
}

# ---------------------------------------------------------------------------
# 7. LAKES
# ---------------------------------------------------------------------------
LAKES = {
    "Attabad Lake": {"province": "Gilgit-Baltistan", "formation": "Formed by the 2010 Hunza landslide dam", "type": "Landslide-dammed lake"},
    "Satpara Lake": {"province": "Gilgit-Baltistan", "formation": "Natural lake, developed with a dam for Skardu water supply", "type": "Reservoir"},
    "Rush Lake": {"province": "Gilgit-Baltistan", "formation": "High-altitude glacial lake near Nagar", "type": "Glacial lake"},
    "Ghizer Lake (Taalidass)": {"province": "Gilgit-Baltistan", "formation": "Site of the 2025 Taalidass GLOF-related event", "type": "Glacial/landslide-influenced lake"},
    "Saif-ul-Malook Lake": {"province": "KPK", "formation": "Glacial lake at the base of Malika Parbat, Kaghan valley", "type": "Glacial lake"},
    "Manchar Lake": {"province": "Sindh", "formation": "Largest natural freshwater lake in Pakistan, fed by the Indus and Aral/Main Nara canals", "type": "Freshwater lake"},
    "Keenjhar Lake": {"province": "Sindh", "formation": "Major freshwater reservoir supplying Karachi and Thatta", "type": "Reservoir lake"},
    "Hanna Lake": {"province": "Balochistan", "formation": "Artificial lake near Quetta", "type": "Reservoir"},
    "Hub Dam Lake": {"province": "Sindh/Balochistan border", "formation": "Reservoir on the Hub River supplying Karachi", "type": "Reservoir"},
    "Khanpur Lake": {"province": "ICT/KPK border", "formation": "Reservoir on the Haro River", "type": "Reservoir"},
    "Banjosa Lake": {"province": "AJK", "formation": "Natural lake near Rawalakot", "type": "Freshwater lake"},
}

# ---------------------------------------------------------------------------
# 7B. DESERTS
# ---------------------------------------------------------------------------
DESERTS = {
    "Thar Desert (Great Indian Desert)": {
        "province": "Sindh",
        "area_km2": 22000,
        "type": "Subtropical arid (sandy) desert",
        "characteristics": (
            "Pakistan's largest desert, covering Tharparkar and Umerkot districts and "
            "extending across the border into India. Semi-arid with monsoon-dependent "
            "seasonal grazing and rain-fed ('barani') farming; home to the Thar Coalfield, "
            "one of the world's largest lignite coal deposits, now feeding coal-power projects."
        ),
    },
    "Cholistan Desert (Rohi)": {
        "province": "Punjab",
        "area_km2": 26000,
        "type": "Subtropical arid (sandy) desert",
        "characteristics": (
            "Stretches along the Pakistan-India border south of Bahawalpur, following the "
            "dried-up bed of the ancient Hakra/Ghaggar river. Dotted with historic forts "
            "(Derawar Fort) along a former caravan route, and hosts the annual Cholistan "
            "Jeep Rally and Desert Festival."
        ),
    },
    "Kharan Desert": {
        "province": "Balochistan",
        "area_km2": 33000,
        "type": "Rocky/sandy basin desert",
        "characteristics": (
            "A closed inland-drainage basin in western Balochistan around Kharan district. "
            "Fed by seasonal flows from the Mashkel and other hill-torrent rivers that "
            "terminate in the Hamun-e-Mashkel salt marsh rather than reaching the sea."
        ),
    },
    "Thal Desert": {
        "province": "Punjab",
        "area_km2": 19000,
        "type": "Subtropical arid (sandy) desert",
        "characteristics": (
            "Lies in the Indus-Jhelum/Chenab doab of central Punjab. Substantially "
            "reclaimed for irrigated agriculture since the mid-20th-century Thal "
            "Development Project, though large tracts of dunes remain in its core."
        ),
    },
    "Katpana Cold Desert": {
        "province": "Gilgit-Baltistan",
        "area_km2": None,
        "type": "High-altitude cold desert",
        "characteristics": (
            "A rare high-altitude cold desert near Skardu (~2,226 m), with active sand "
            "dunes set against a backdrop of snow-capped Karakoram peaks — a notable "
            "geomorphological curiosity and increasingly popular tourist stop."
        ),
    },
}

# ---------------------------------------------------------------------------
# 8. NATIONAL DISASTER RISK CONTEXT
# ---------------------------------------------------------------------------
DISASTER_HAZARD_PROFILE = {
    "A. Hydro-meteorological Hazards": {
        "Floods": {
            "Riverine Floods": "Large-scale overbank flooding along the Indus and its tributaries, typically monsoon-driven (e.g., 2010, 2022 floods).",
            "Flash Floods / Hill Torrents": "Sudden, high-velocity flows from Balochistan/Sulaiman/Kirthar hill torrents and steep KPK/GB valleys.",
            "Urban Flooding": "Drainage-system failure in cities like Karachi and Lahore during intense short-duration rainfall.",
            "Mudflows": "Saturated slope debris flows in northern mountain valleys after intense rain or glacial outburst.",
            "Cloudbursts": "Highly localized, extremely intense rainfall events increasingly reported in GB/KPK and monsoon-affected hill zones.",
        },
        "Monsoon Variability": "Erratic onset, intensity and withdrawal of the summer monsoon, producing both localized flooding and prolonged dry spells.",
        "Droughts": "Recurrent in Balochistan, Sindh (Tharparkar) and southern Punjab, driven by rainfall deficits and reduced river/canal supply.",
        "GLOFs": "Glacial Lake Outburst Floods from moraine- or ice-dammed lakes in GB and northern KPK, a rapidly growing risk under warming.",
        "Heatwaves": "Intense pre-monsoon heat events affecting Sindh and southern Punjab, with public-health and energy-demand impacts.",
        "Water Stress": "Growing gap between water availability and demand across the Indus Basin, worsened by inefficient use and storage shortfalls.",
    },
    "B. Pakistan's Tectonic Setting": {
        "Earthquakes": "High seismicity along the Chaman, Main Boundary and Main Karakoram Thrust fault systems (e.g., 2005 Kashmir earthquake).",
        "Landslides": "Common in GB, KPK and AJK, often triggered by seismic activity, rainfall or slope undercutting from river erosion.",
        "Avalanches": "Snow avalanches in high-altitude Karakoram/Himalaya/Hindu Kush terrain, a hazard to roads (e.g., Karakoram Highway) and settlements.",
        "Tsunamis": "Low-probability but non-zero risk along the Makran coast, linked to the Makran Subduction Zone (1945 Makran tsunami precedent).",
        "Seismic Activity and Land Shifts": "Ongoing crustal deformation from the India-Eurasia collision affecting infrastructure stability in the north.",
        "Snow Contingencies": "Heavy snowfall events isolating northern communities and disrupting the Karakoram Highway and mountain passes.",
    },
    "C. Climatological & Emerging Hazards": {
        "Accelerated Glacier Melt": "Warming-driven retreat and destabilization of Karakoram/Himalaya/Hindu Kush glaciers, feeding GLOF risk and altering river regimes.",
        "Sea-Level Rise and Cyclones": "Rising Arabian Sea levels and increasing cyclone activity threatening the Sindh/Balochistan coastline.",
        "Smog": "Seasonal (autumn-winter) air-quality crisis concentrated in Punjab's urban corridor (Lahore-Faisalabad).",
        "Pollution (Air, Water, Soil)": "Industrial effluent, agricultural runoff and vehicular emissions degrading air, surface/groundwater and soil quality.",
        "Unpredictably Erratic Global Climate Patterns": "Broader climate-change-driven variability compounding all of the above hazard categories.",
    },
    "D. Anthropogenic Hazards": {
        "Industrial Accidents and Chemical Spills": "Risks concentrated in industrial clusters (Karachi, Faisalabad, Sialkot) with limited hazardous-material regulation.",
        "Transport and Infrastructure Risks": "Road, rail and bridge failures, often flood- or landslide-triggered, especially on mountain highways.",
        "Maritime Disasters": "Shipping and port-related incidents along the Karachi/Gwadar coastline.",
        "Oil Spills": "Risk associated with port operations and coastal shipping lanes near Karachi and Gwadar.",
        "Fires": "Urban structural fires, wildfires in forested northern/western regions, and industrial fires.",
        "Encroachments": "Unregulated construction on floodplains, riverbeds and drainage channels, amplifying flood exposure.",
        "Food Security": "Vulnerability of crop production to floods, droughts and water disputes, affecting national food supply.",
        "Population Bulge": "Rapid population growth increasing exposure and straining infrastructure and disaster response capacity.",
        "Biological Hazards": "Epidemic/disease outbreak risk, often compounded by post-flood waterborne and vector-borne illness.",
    },
}

DISASTER_EXPOSURE_VULNERABILITY = {
    "Population Pressure and Diverse Terrains": "Rapid urban growth combined with highly varied terrain (coast, plains, mountains, deserts) multiplies hazard exposure pathways.",
    "Vulnerable Settlements and Infrastructure Deficits": "Informal settlements, weak building codes and inadequate drainage/flood-protection infrastructure raise disaster losses.",
    "Institutional Vulnerabilities": {
        "Delayed Decision-Making": "Slow inter-agency coordination during disaster response.",
        "Operational Confusion": "Overlapping mandates between federal, provincial and district disaster bodies.",
        "Public Distrust": "Erosion of public confidence in early-warning and relief systems after past response failures.",
        "Resource Misallocation": "Inefficient targeting of relief and reconstruction funds.",
    },
    "Socio-Economic Stratification Amplifying Risk": {
        "drivers": ["Poverty", "Income inequality", "Limited access to education, healthcare and emergency resources",
                    "Resource disparities", "Spatial entrapment", "Unequal mobility",
                    "Marginalized communities", "Poor households", "Institutional neglect"],
        "summary": "Poorer and marginalized communities are disproportionately located in high-hazard zones (floodplains, hill-torrent paths, coastal fringes) with the least capacity to prepare, evacuate or recover.",
    },
}

DISASTER_EMERGING_RISKS = {
    "Global Climate Risk Index (CRI) 2025": "Pakistan continues to rank among the countries most affected by climate-related extreme weather events over the past two decades, per Germanwatch's Global Climate Risk Index series.",
    "Increasing GLOF Risks": (
        "Rising temperatures are destabilizing moraine-dammed lakes, increasing the likelihood of sudden breaches. "
        "GLOFs threaten downstream settlements, hydroelectric infrastructure and road networks such as the Karakoram "
        "Highway. GB and parts of KP are seeing an alarming rise in glacial lake formation due to accelerated glacier "
        "melt. The 2025 Taalidass/Ghizer Lake event and the 2010 Attabad Lake disaster underline the need for proactive "
        "mitigation, remote-sensing and in-situ hydrological monitoring, and community-level early-warning systems."
    ),
    "Erratic Monsoons and Shifting Precipitation Patterns": (
        "The monsoon system is becoming increasingly unpredictable: early onset and extended seasons, uneven rainfall "
        "distribution (the 'short-burst' phenomenon), and high-intensity weather (localized cloudbursts, intense "
        "downpours, sudden hailstorms and atmospheric instability) are now common — resulting in localized flash "
        "floods, cloudbursts, mudflows, riverine flooding and soil erosion."
    ),
    "Sea Intrusion and Coastal Salinization": (
        "Rising sea levels along Pakistan's 1,050 km coastal belt are compounding flood risk in low-lying areas, "
        "particularly southern Sindh and Balochistan. Saltwater intrusion into freshwater aquifers is degrading "
        "arable land and threatening agriculture- and aquaculture-dependent livelihoods. Karachi, Gwadar and Thatta "
        "face increased vulnerability to tidal surges and cyclonic activity, amplified by poor drainage infrastructure "
        "and rapid urbanization. Integrated coastal zone management, mangrove restoration and improved storm-surge "
        "early-warning systems are critical mitigation priorities."
    ),
}

DISASTER_RISK_SCENARIOS = {
    "Baseline Scenario": {
        "description": "Current trajectory: incremental improvements in early-warning systems and disaster funding but no major structural change.",
        "features": ["Recurring seasonal flood/drought cycles", "Gradual glacier retreat", "Slow adaptation-financing uptake", "Localized, manageable disaster losses in most years"],
    },
    "Medium Scenario": {
        "description": "Accelerated climate variability outpaces current adaptive capacity in several provinces.",
        "features": ["More frequent GLOFs and flash floods", "Growing water stress between provinces", "Rising urban flooding and smog severity", "Increased internal displacement in high-risk districts"],
    },
    "Worst-Case Scenario": {
        "description": "Compounding hazards (major riverine flood + GLOF + cyclone + drought in different regions concurrently) overwhelm national response capacity.",
        "features": ["Simultaneous multi-hazard events straining NDMA/PDMA resources", "Severe agricultural and food-security shocks", "Major infrastructure loss (roads, power, irrigation)", "Large-scale displacement and cross-provincial water-sharing conflict"],
    },
}

# ---------------------------------------------------------------------------
# 8b. HISTORICAL DISASTER EVENTS (illustrative timeline)
# ---------------------------------------------------------------------------
DISASTER_HISTORICAL_EVENTS = [
    {
        "year": 1935,
        "name": "Quetta Earthquake",
        "hazard_type": "Earthquake",
        "provinces": ["Balochistan"],
        "summary": "One of the deadliest earthquakes in South Asian history, devastating Quetta city; a major driver of modern seismic building-code awareness in Pakistan.",
    },
    {
        "year": 1945,
        "name": "Makran Tsunami",
        "hazard_type": "Tsunami",
        "provinces": ["Balochistan", "Sindh"],
        "summary": "Triggered by a major offshore earthquake on the Makran Subduction Zone; struck the coastal belt and remains the key historical precedent for Pakistan's (low-probability but real) tsunami risk.",
    },
    {
        "year": 2005,
        "name": "Kashmir Earthquake",
        "hazard_type": "Earthquake",
        "provinces": ["AJK", "KPK"],
        "summary": "Magnitude ~7.6 earthquake centered near Muzaffarabad; one of the deadliest natural disasters in Pakistan's history, exposing major gaps in seismic building standards and triggering national disaster-management reforms (leading to NDMA's creation).",
    },
    {
        "year": 2010,
        "name": "Attabad Lake Landslide & Outburst Risk",
        "hazard_type": "Landslide-dammed lake / GLOF-adjacent",
        "provinces": ["Gilgit-Baltistan"],
        "summary": "A massive landslide in Hunza blocked the Hunza River, forming Attabad Lake, submerging villages and the Karakoram Highway, and creating an ongoing outburst-flood risk that reshaped local infrastructure planning.",
    },
    {
        "year": 2010,
        "name": "2010 Pakistan Floods",
        "hazard_type": "Riverine flood",
        "provinces": ["KPK", "Punjab", "Sindh", "Balochistan"],
        "summary": "Among the most severe floods in Pakistan's recorded history, triggered by exceptionally heavy monsoon rainfall; affected roughly a fifth of the country's land area and displaced millions.",
    },
    {
        "year": 2022,
        "name": "2022 Pakistan Floods",
        "hazard_type": "Riverine & flash flood",
        "provinces": ["Sindh", "Balochistan", "KPK", "Punjab", "Gilgit-Baltistan"],
        "summary": "Record monsoon rainfall combined with glacial melt produced catastrophic flooding across roughly a third of the country; among the costliest disasters in Pakistan's history in both humanitarian and economic terms.",
    },
    {
        "year": 2025,
        "name": "Taalidass / Ghizer Lake Event",
        "hazard_type": "GLOF-related",
        "provinces": ["Gilgit-Baltistan"],
        "summary": "A glacial lake event in the Ghizer district highlighted the accelerating pace of glacial lake formation and outburst risk in GB, reinforcing calls for expanded remote-sensing monitoring and community early-warning systems.",
    },
]

DISASTER_HAZARD_BY_PROVINCE = {
    "Gilgit-Baltistan": ["GLOFs", "Landslides", "Avalanches", "Earthquakes", "Snow contingencies", "Accelerated glacier melt"],
    "KPK": ["Flash floods / hill torrents", "Riverine floods", "Earthquakes", "Landslides", "Monsoon variability"],
    "Punjab": ["Riverine floods", "Urban flooding", "Smog", "Heatwaves", "Water stress"],
    "Sindh": ["Riverine floods", "Droughts", "Heatwaves", "Sea-level rise / coastal salinization", "Water stress"],
    "Balochistan": ["Droughts", "Flash floods / hill torrents", "Earthquakes", "Tsunamis (coastal)", "Water stress"],
    "AJK": ["Earthquakes", "Landslides", "Flash floods", "Avalanches"],
    "ICT": ["Urban flooding", "Smog", "Landslides (Margalla Hills, minor)"],
}

# ---------------------------------------------------------------------------
# 9. SOCIO-ECONOMIC & AGRO-ECONOMIC DOMAINS
# ---------------------------------------------------------------------------
SOCIO_ECONOMIC_DOMAIN = {
    "Food Security": "Rivers and canal-fed irrigation underpin national staple-crop production (wheat, rice, sugarcane); disruptions directly threaten food availability.",
    "Employment": "Agriculture, fisheries and hydropower construction/operations provide large-scale rural and semi-skilled employment.",
    "Urban Growth": "River corridors and canal commands have historically shaped the location and growth of Pakistan's major cities.",
    "Tourism": "Northern rivers, lakes and mountain ranges (GB, KPK, AJK) are core assets for domestic and international tourism.",
    "Domestic & Industrial Utility": "Rivers and reservoirs supply municipal water and industrial process water to major urban centers.",
    "Climate & Vulnerability": "Water availability variability directly links to climate vulnerability across all provinces, especially arid and coastal zones.",
    "Energy Generation": "Hydropower (Tarbela, Mangla, CPEC run-of-river projects) supplies a substantial share of national electricity generation.",
}

AGRO_ECONOMIC_DOMAIN = {
    "World's Largest Contiguous Irrigation System (IBIS)": "The Indus Basin Irrigation System is widely cited as the world's largest contiguous irrigation network, built around the Indus, Jhelum, Chenab, Ravi and Sutlej rivers and their link-canal system.",
    "Crop Cultivation": "Supports wheat, cotton, rice and sugarcane cultivation across Punjab and Sindh, the backbone of Pakistan's agrarian economy.",
    "Rural Livelihoods": "The majority of Pakistan's rural population depends directly or indirectly on canal-irrigated agriculture.",
    "GDP & Employment Contribution": "Agriculture contributes a significant share of national GDP and remains one of the largest employment sectors in the country.",
}

# ---------------------------------------------------------------------------
# 10. GEO-POLITICAL & STRATEGIC DOMAINS
# ---------------------------------------------------------------------------
GEOPOLITICAL_DOMAIN = {
    "The Hydro-Politics of Kashmir": (
        "Kashmir's location at the headwaters of the Jhelum and Chenab rivers makes it central to India-Pakistan "
        "water relations; upstream infrastructure decisions in Indian-administered Kashmir have direct downstream "
        "implications for AJK and Punjab."
    ),
    "The Indus Waters Treaty (IWT) Crisis": (
        "The 1960 IWT allocated the eastern rivers (Ravi, Sutlej, Beas) to India and the western rivers (Indus, "
        "Jhelum, Chenab) to Pakistan, with India retaining limited run-of-river hydropower rights on the western "
        "rivers. Recent years have seen the treaty's implementation mechanisms come under strain amid broader "
        "bilateral tensions, with disputes over the design of Indian hydropower projects on the western rivers."
    ),
    "Maritime Trade Infrastructure": (
        "Karachi Port, Port Qasim and the CPEC-linked Gwadar Port anchor Pakistan's maritime trade and are "
        "increasingly tied to river-basin and coastal-zone management given sea-intrusion and siltation pressures."
    ),
}

INTERNAL_WATER_DISPUTES = {
    "overview": "Beyond the international dimension, Pakistan faces persistent inter-provincial disputes over Indus water distribution, chiefly between upper-riparian Punjab and lower-riparian Sindh.",
    "Sindh's Grievances (Lower Riparian)": (
        "Sindh argues that upstream withdrawals and new canal proposals reduce flows reaching the province, "
        "threatening Indus delta ecology, the Manchar/Keenjhar lake systems, and the '10-day flow' guarantees "
        "envisioned in the 1991 Water Apportionment Accord."
    ),
    "Punjab's Counter-Claims (Upper Riparian)": (
        "Punjab maintains that its allocations follow the 1991 Accord formula and that new storage/canal projects "
        "(e.g., proposed corporate agriculture canal schemes) are needed for national food security and do not "
        "breach Sindh's entitlements."
    ),
    "Structural Gridlocks / Deadlock": (
        "Disagreement over telemetry data accuracy, the pace of new storage construction, and Punjab's proposed "
        "canal projects has repeatedly stalled consensus within IRSA and the CCI."
    ),
    "Environmental Impacts of Indian Chenab Projects on Punjab's Crops": {
        "Flow Reductions at Head Marala": "Pakistani officials have periodically reported reduced and irregular flows at Marala Headworks, attributed in part to upstream Indian operations on the Chenab.",
        "Devastating Crop Impacts": "Reduced or unpredictable Chenab flows affect sowing schedules and yields for Punjab's Rabi and Kharif crops in the Chenab command area.",
    },
}

IRSA_LEGAL_MECHANISMS = {
    "IRSA Technocratic Vote Deadlock": "The Indus River System Authority's provincial-member voting structure has at times produced deadlock on distribution disputes, particularly around telemetry and shortage-sharing formulas.",
    "Council of Common Interests (CCI) Appeal": "Unresolved IRSA disputes are escalated to the CCI, the constitutional forum for resolving inter-provincial disagreements on shared resources.",
    "Constitutional Review (Supreme Court)": "In some cases, provinces have sought judicial review of water-distribution or canal-project decisions before the Supreme Court of Pakistan.",
    "The 2024-2026 Restructuring Crisis": "Renewed debate over IRSA's composition, voting weight and the 1991 Accord's implementation has driven proposals to restructure the authority's decision-making process.",
    "The Veto Power and Conciliation": "Discussions have centered on whether any single province should hold an effective veto over shared-water decisions, versus consensus-based conciliation mechanisms.",
    "Judicial Intervention": "Courts have occasionally been asked to adjudicate procedural disputes (e.g., environmental clearance requirements for new canal projects) rather than the underlying allocation formula itself.",
}

# ---------------------------------------------------------------------------
# 11. CHINA'S HYDROPOWER INVESTMENT FOOTPRINT (CPEC)
# ---------------------------------------------------------------------------
CHINA_HYDROPOWER_FOOTPRINT = {
    "Dominant Share of FDI": (
        "Hydropower and broader energy projects have historically represented one of the largest single categories "
        "of Chinese foreign direct investment into Pakistan under CPEC, reflecting the strategic priority placed on "
        "addressing the country's electricity generation shortfall."
    ),
    "Major Hydropower Asset Portfolio": {
        "Karot Hydropower Project": {"capacity_MW": 720, "river": "Jhelum River", "status": "Operational (2022)", "notes": "First hydropower project financed under the CPEC framework; run-of-river design."},
        "Suki Kinari (SK) Hydropower Station": {"capacity_MW": 884, "river": "Kunhar River", "status": "Operational (2024)", "notes": "Located in KPK's Kaghan valley; faced construction delays and security-related cost escalation."},
        "Kohala Hydropower Project": {"capacity_MW": 1124, "river": "Jhelum River", "status": "Under development", "notes": "One of the largest planned private-sector hydropower investments in Pakistan."},
        "Azad Pattan Hydropower Project": {"capacity_MW": 700.7, "river": "Jhelum River", "status": "Under development", "notes": "Run-of-river project in AJK; financing and implementation timelines have faced periodic revision."},
    },
}

# ---------------------------------------------------------------------------
# 12. INDIA'S UPSTREAM DAM DESIGN DISPUTES (Chenab tributaries)
# ---------------------------------------------------------------------------
INDIA_DAM_DESIGN_DISPUTES = {
    "Pakal Dul Dam": {"capacity_MW": 1000, "river": "Marusudar River (Chenab tributary)", "location": "Indian-administered Jammu & Kashmir"},
    "Ratle Dam": {"capacity_MW": 850, "river": "Chenab River", "location": "Indian-administered Jammu & Kashmir"},
    "technical_points_of_contention": {
        "Pondage Capacity": {
            "issue": "The volume of water a run-of-river plant can hold behind its dam for short-term regulation.",
            "pakistan_view": "Pakistan contends that the pondage allowed under the IWT's technical criteria for run-of-river plants is being exceeded or interpreted too liberally, enabling India greater short-term control over downstream flow timing.",
        },
        "Freeboard Height & Dam Elevation": {
            "issue": "The margin of dam height above maximum water level, and overall structure elevation.",
            "pakistan_view": "Pakistan argues higher-than-necessary freeboard and dam elevation could allow greater storage capability than the 'run-of-river' classification permits under the treaty.",
        },
        "Deep-Level Outlets and Gated Spillways": {
            "issue": "Low-level outlets and gated (rather than ungated/fixed) spillways affect a dam's ability to flush sediment and regulate flow.",
            "pakistan_view": "Pakistan has raised concerns that gated spillways and deep-level outlets give India operational flexibility to manipulate downstream flow timing beyond what the treaty's technical annexures intend.",
        },
        "Court of Arbitration (CoA) Interventions": (
            "Pakistan has pursued international arbitration (Permanent Court of Arbitration, following the Kishenganga "
            "precedent) over the design parameters of projects like Kishenganga, Ratle and Pakal Dul, while India has "
            "favored the Neutral Expert mechanism under the treaty; the parallel-track dispute-resolution process "
            "itself has become a point of procedural contention between the two states."
        ),
    },
}

# ---------------------------------------------------------------------------
# 13. SOURCES / REFERENCES
# ---------------------------------------------------------------------------
# Primary/official references backing the geopolitical, CPEC and IBIS content
# above. Grouped by topic for display in the app's "Sources" section.
SOURCES = {
    "Indus Waters Treaty & Arbitration": [
        {
            "label": "PCA — Indus Waters Western Rivers Arbitration (Pakistan v. India)",
            "url": "https://pca-cpa.org/en/cases/284/",
        },
        {
            "label": "PCA — June 2025 Supplemental Award on Competence",
            "url": "https://pca-cpa.org/en/news/pca-press-release-pca-case-no-2023-01-proceedings-under-the-indus-waters-treaty-islamic-republic-of-pakistan-v-republic-of-india-3/",
        },
    ],
    "CPEC Hydropower Projects": [
        {
            "label": "PPIB — CPEC Projects (updated June 30, 2026)",
            "url": "https://www.ppib.gov.pk/cpec.html",
        },
        {
            "label": "CPEC — Energy Projects",
            "url": "https://cpec.gov.pk/energy",
        },
        {
            "label": "CPEC — Karot Hydropower Project",
            "url": "https://cpec.gov.pk/project-details/16",
        },
        {
            "label": "CPEC — Suki Kinari Hydropower Project",
            "url": "https://cpec.gov.pk/project-details/15",
        },
        {
            "label": "CPEC — Kohala Hydropower Project",
            "url": "https://www.cpec.gov.pk/project-details/23",
        },
        {
            "label": "CPEC — Azad Pattan Hydropower Project",
            "url": "https://cpec.gov.pk/project-details/91",
        },
    ],
    "Dams & Water Governance": [
        {
            "label": "WAPDA — Diamer-Bhasha Dam Project",
            "url": "https://wapda.gov.pk/diamer-basha-dam-project/",
        },
        {
            "label": "Ministry of Economic Affairs — Diamer-Bhasha clarification, 29 Aug 2026",
            "url": "https://www.ead.gov.pk/NewsDetail/ODI1M2E0ODYtMjkyMi00NzdkLWE2ODQtMDk5NWIwZGY4YmE1",
        },
        {
            "label": "CCI — Functions / Article 155",
            "url": "https://www.cci.gov.pk/Detail/NDZhY2I2ZDUtZTgzNy00MWEzLWE2M2ItZjU2NTkyODc4ZGJm",
        },
    ],
    "Indus Basin Irrigation System": [
        {
            "label": "World Bank — Indus Basin groundwater / IBIS",
            "url": "https://www.worldbank.org/en/news/feature/2021/03/25/managing-groundwater-resources-in-pakistan-indus-basin",
        },
    ],
}
