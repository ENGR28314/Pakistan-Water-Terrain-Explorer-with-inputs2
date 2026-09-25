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
# 9B. MAJOR CROP SEASONS — RABI & KHARIF
# ---------------------------------------------------------------------------
CROP_SEASONS = {
    "Rabi (Winter) Season": {
        "sowing_window": "October – December",
        "harvest_window": "March – May",
        "description": (
            "Pakistan's winter cropping season, sown after the monsoon using stored canal/reservoir water and "
            "residual soil moisture, and harvested before the summer heat and monsoon onset."
        ),
        "major_crops": {
            "Wheat": "The dominant Rabi staple and Pakistan's most important food crop, grown mainly across Punjab and Sindh's canal commands.",
            "Gram (Chickpea)": "A major Rabi pulse, largely rain-fed/'barani' in Punjab's Thal and Potohar tracts and parts of Balochistan.",
            "Lentil (Masoor)": "Grown on a smaller area alongside gram as a Rabi pulse crop.",
            "Barley": "Grown in marginal and rain-fed areas, including parts of Punjab and Balochistan.",
            "Mustard / Rapeseed (Canola)": "A Rabi oilseed crop grown across Punjab and Sindh to supply the edible-oil industry.",
            "Tobacco (Rabi crop in KPK)": "Grown mainly in Khyber Pakhtunkhwa's Swabi, Mardan and Buner districts.",
            "Potato (autumn/Rabi crop)": "Grown as an autumn/Rabi crop in Punjab in addition to its main spring season.",
        },
    },
    "Kharif (Summer/Monsoon) Season": {
        "sowing_window": "April – June",
        "harvest_window": "October – December",
        "description": (
            "Pakistan's summer/monsoon cropping season, sown ahead of or during the monsoon and relying heavily "
            "on peak-season canal supplies from the Indus system."
        ),
        "major_crops": {
            "Cotton": "A key Kharif cash crop and the backbone of Pakistan's textile export industry, concentrated in Punjab and Sindh.",
            "Rice": "Grown in the canal commands of Punjab (notably basmati in the Kalar tract) and Sindh; a major export earner.",
            "Sugarcane": "A water-intensive Kharif cash crop grown across Punjab, Sindh and parts of KPK, feeding the domestic sugar industry.",
            "Maize (Corn)": "Grown mainly in Punjab (Chiniot, Sahiwal belt) and Khyber Pakhtunkhwa, for both food and feed use.",
            "Bajra (Pearl Millet)": "A drought-tolerant Kharif staple grown chiefly on rain-fed land in Sindh and southern Punjab.",
            "Jowar (Sorghum)": "Grown as a Kharif fodder and grain crop, mostly rain-fed, in Punjab and Sindh.",
            "Groundnut": "A Kharif oilseed grown mainly on the rain-fed Potohar Plateau of Punjab.",
        },
    },
}

# ---------------------------------------------------------------------------
# 9C. ALLIED AGRICULTURE SECTORS — APICULTURE & AQUACULTURE
# ---------------------------------------------------------------------------
ALLIED_AGRI_SECTORS = {
    "Apiculture (Beekeeping)": {
        "overview": (
            "A growing allied sub-sector built mainly around the European honeybee (Apis mellifera), "
            "introduced alongside the native Apis cerana and Apis florea, providing rural income, honey "
            "production and crop-pollination services."
        ),
        "key_regions": "Khyber Pakhtunkhwa (Malakand, Swat, Mansehra), Punjab (Potohar and canal-irrigated districts), and parts of Azad Jammu & Kashmir and Balochistan.",
        "economic_role": (
            "Supports smallholder and migratory beekeeping enterprises producing honey for domestic consumption "
            "and export, and improves yields in pollination-dependent crops such as mustard, sunflower and fruit orchards."
        ),
        "challenges": "Pesticide exposure, habitat/floral loss, disease and parasite pressure (e.g. Varroa mites), and climate variability affecting bloom timing.",
    },
    "Aquaculture & Fisheries": {
        "overview": (
            "Encompasses freshwater fish farming fed by the canal/reservoir network, brackish-water/coastal "
            "shrimp and fish farming, and cold-water trout farming in the northern mountain streams."
        ),
        "key_regions": (
            "Freshwater carp culture is concentrated in Punjab and Sindh (fed by canals and reservoirs such as "
            "Tarbela and Mangla); brackish-water shrimp and fish farming occurs along the Sindh and Balochistan "
            "coast and in the Indus Delta; trout farming is practiced in the cold streams of KPK, GB and AJK."
        ),
        "species": "Major carps (rohu, catla, mrigal) in freshwater ponds; shrimp/prawn and marine fish species along the coast; rainbow and brown trout in northern hatcheries.",
        "economic_role": (
            "A source of rural livelihoods and protein supply, and a modest but growing export sector "
            "(particularly seafood/shrimp), though it remains far smaller than crop agriculture in overall GDP share."
        ),
        "challenges": "Reduced freshwater/silt inflow to the Indus Delta affecting coastal fisheries and mangrove nurseries, water quality, and limited adoption of modern hatchery and feed technology.",
    },
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

# ---------------------------------------------------------------------------
# 14. FORESTS OF PAKISTAN
# ---------------------------------------------------------------------------
FOREST_TYPES = {
    "Coniferous Forests": {
        "regions": "Northern mountainous areas of Khyber Pakhtunkhwa and Gilgit-Baltistan (Swat, Dir, Kaghan, Chitral, Hazara)",
        "altitude": "1,000 to 4,000 meters",
        "species": "Pine (chir pine, blue pine), fir (pindrow fir), spruce and deodar — Pakistan's national tree",
        "notes": (
            "Pakistan's largest natural forest category by area, forming the backbone of the country's timber "
            "and watershed-protection resources; zoned by altitude from chir pine at lower elevations to fir "
            "and spruce near the timberline."
        ),
    },
    "Mangrove Forests": {
        "regions": "Coastal wetlands of the Indus Delta near Karachi (Sindh) and the Balochistan coast, along the Arabian Sea",
        "altitude": "Sea level (tidal creeks and delta)",
        "species": "Predominantly grey/white mangrove (Avicennia marina), with small stands of other species",
        "notes": (
            "Among the largest arid-climate mangrove ecosystems in the world; protect the coastline from erosion "
            "and storm surge, support fisheries and shrimp nurseries, but face pressure from reduced freshwater "
            "and silt inflow from the Indus and from coastal urbanization."
        ),
    },
    "Riverain (Bela) Forests": {
        "regions": "Narrow strips along the active floodplain (\"bela\") of the Indus River and its tributaries, chiefly in Punjab and Sindh",
        "altitude": "Lowland floodplain",
        "species": "Sheesham (Dalbergia sissoo), kikar/babul (Acacia nilotica), tamarisk and reed beds",
        "notes": (
            "Dependent on seasonal Indus flooding to regenerate; provide fuelwood, fodder and habitat corridors "
            "along the river, but have shrunk with upstream flow regulation, barrages and encroachment."
        ),
    },
    "Tropical Thorn (Scrub) Forests": {
        "regions": "Low-lying plains and semi-arid flatlands of Punjab and Sindh, including the Potohar Plateau and parts of the Salt Range",
        "altitude": "Plains (roughly 200–500 m)",
        "species": "Acacia (kikar), Prosopis (jand/mesquite), Capparis (karir) and other drought-tolerant thorny shrubs and small trees",
        "notes": (
            "Open, sparse woodland adapted to low and erratic rainfall; historically grazed and cut for fuelwood, "
            "making it one of the more degraded forest types by area."
        ),
    },
    "Irrigated / Planted Forests": {
        "regions": "Man-made plantations on canal-irrigated land in Punjab and Sindh, most famously Changa Manga near Lahore",
        "altitude": "Plains",
        "species": "Sheesham (Dalbergia sissoo), mulberry (Morus alba), kikar (Acacia nilotica), eucalyptus",
        "notes": (
            "Established from the mid-19th century onward — beginning with Changa Manga in 1866 — chiefly to "
            "meet railway-sleeper and general timber demand; among the world's oldest large-scale hand-planted "
            "forests, now also serving as wildlife reserves and recreation sites."
        ),
    },
}

NOTABLE_FORESTS = {
    "Changa Manga Forest": {
        "location": "Kasur and Lahore districts, Punjab (~70–80 km southwest of Lahore, off the N-5 near Chunian/Bhai Pheru)",
        "forest_type": "Irrigated / Planted Forest",
        "covered_area": "About 5,065 hectares (12,500 acres) today, down from a peak of around 8,400 acres originally afforested and later expanded",
        "history_origin": (
            "Planted from 1866 under the British Raj on the recommendation of Dr John Lindsay Stewart, Punjab's "
            "first Conservator of Forests, to supply fuel and timber (sleepers) for the North-Western Railway. "
            "Using a trench-and-ridge irrigation system devised by C. F. Amery and refined by Inspector-General "
            "B. Ribbentrop, it became one of the world's largest and oldest hand-planted forests, once served by "
            "its own narrow-gauge logging railway (from 1870)."
        ),
        "wildlife_nature": (
            "Sheesham, kikar and mulberry plantations support around 14 mammal species (hog deer, jackal, "
            "wild boar, nilgai), roughly 50 bird species including peafowl and vultures, plus reptiles and "
            "amphibians; illegal logging has reduced its extent from its historic peak."
        ),
        "attractions_recreation": (
            "A popular day-trip destination from Lahore for picnicking, cycling and camping, with a small "
            "heritage narrow-gauge railway, lakes, and a wildlife-breeding area."
        ),
    },
    "Ziarat Juniper Forest": {
        "location": "Ziarat Valley and Mount Zarghoon, Balochistan (about 3 hours from Quetta)",
        "forest_type": "Coniferous Forest (dry temperate juniper)",
        "covered_area": "Roughly 110,000 hectares (some estimates put the wider biosphere reserve near 247,000 acres)",
        "history_origin": (
            "Pakistan's largest contiguous juniper (Juniperus excelsa) forest and believed to be the second-"
            "largest juniper forest in the world after California's; some trees are estimated at over 1,500 "
            "years old (some claims run into the thousands). Designated a UNESCO Biosphere Reserve in 2013 and "
            "on Pakistan's tentative UNESCO World Heritage list since 2016."
        ),
        "wildlife_nature": (
            "Slow-growing juniper stands between about 1,180 and 3,490 meters elevation host the Himalayan "
            "black bear, markhor and a range of birds; the forest is a globally significant carbon sink but "
            "faces threats from climate change, grazing pressure, illegal cutting and disease."
        ),
        "attractions_recreation": (
            "Hiking among centuries-old 'living fossil' junipers, cool highland scenery, and proximity to "
            "Ziarat's Quaid-e-Azam Residency; best visited April–October."
        ),
    },
    "Ushu Forest": {
        "location": "Ushu (Usho) Valley, north of Kalam, Upper Swat District, Khyber Pakhtunkhwa",
        "forest_type": "Coniferous Forest",
        "covered_area": "Roughly 18,000 hectares",
        "history_origin": (
            "A dense natural coniferous forest along the Ushu Khwar river valley, historically used for timber "
            "and grazing by local Swati communities; it lies on the route between Kalam town and Mahodand Lake."
        ),
        "wildlife_nature": (
            "Dominated by deodar (Pakistan's national tree), blue pine and spruce, with wild rose, juniper and "
            "Himalayan yew understorey; home to elusive species such as musk deer, Himalayan black bear, red "
            "fox and birds including woodpeckers and the Himalayan monal."
        ),
        "attractions_recreation": (
            "Trekking routes including the multi-day Ushu Glacier trek, riverside camping and picnicking, and "
            "the scenic drive/hike onward to Mahodand Lake."
        ),
    },
    "Dir Forest (Kumrat Valley)": {
        "location": "Upper Dir District, Khyber Pakhtunkhwa (Kumrat Valley, along the Panjkora River)",
        "forest_type": "Coniferous Forest",
        "covered_area": "Extensive valley-floor and slope forest along the Panjkora River (exact hectarage not consistently documented)",
        "history_origin": (
            "Part of the historic Dir Kohistan forest tracts long managed for timber under the former State of "
            "Dir and, since 1969, Khyber Pakhtunkhwa's forest administration; the Kumrat Valley has become one "
            "of the province's fastest-growing tourist destinations in recent years."
        ),
        "wildlife_nature": (
            "Towering deodar stands on the valley floor give way to blue pine and West Himalayan fir higher up, "
            "with oak forest in the lower valley; wildlife includes the Asiatic black bear, gray wolf, red fox, "
            "yellow-throated marten and Kashmir musk deer."
        ),
        "attractions_recreation": (
            "Waterfalls, the Kala Chashma (Black Spring), riverside camping on the Panjkora, and 4x4 jeep tracks "
            "drawing roughly a million summer visitors to the wider Kumrat area."
        ),
    },
    "Soon Valley Forest": {
        "location": "Khushab District, Punjab (Salt Range, around Sakesar peak)",
        "forest_type": "Sub-tropical scrub / dry forest",
        "covered_area": "Valley spans about 780 km² (56 km long, ~14 km wide); forest cover concentrated on the surrounding Salt Range hills",
        "history_origin": (
            "A historic Salt Range valley long settled by the Janjua and Awan communities; its slopes were "
            "progressively afforested and protected around the Sakesar ridge, the highest point in the Salt "
            "Range at 1,525 m."
        ),
        "wildlife_nature": (
            "The valley's Uchhali, Khabeki and Jahlar lakes form the Ramsar-listed Uchhali Complex wetland, "
            "wintering ground for thousands of migratory waterfowl including the rare white-headed duck; forested "
            "slopes shelter chinkara, wild boar and a variety of birdlife."
        ),
        "attractions_recreation": (
            "Boating and birdwatching at Uchhali and Khabeki lakes, the Kanhatti Garden waterfalls, hiking around "
            "Sakesar, and historic forts (Akrand, Tulhath) and shrines within the valley."
        ),
    },
    "Mukshpuri Forest": {
        "location": "Mukshpuri peak, Nathiagali area, Abbottabad District, Khyber Pakhtunkhwa",
        "forest_type": "Coniferous Forest (moist temperate)",
        "covered_area": "Part of the wider Ayubia National Park / Nathiagali forest tract (Ayubia NP covers about 3,312 hectares)",
        "history_origin": (
            "Forested hill forming part of the Galyat forest belt developed as a hill-station retreat under "
            "British colonial administration; now managed jointly with the adjacent Ayubia National Park."
        ),
        "wildlife_nature": (
            "Dense fir, spruce, pine and oak forest sheltering the common leopard, Himalayan palm civet, kalij "
            "pheasant and a rich songbird population; part of a key west Himalayan biodiversity corridor with "
            "Miranjani and Ayubia."
        ),
        "attractions_recreation": (
            "A popular day hike (Mukshpuri Top trail) from Nathiagali offering panoramic Galyat views; a "
            "staging point on the longer Mukshpuri–Miranjani ridge trek."
        ),
    },
    "Rama Meadows Forest": {
        "location": "Rama Valley, above Astore, Gilgit-Baltistan (base-camp side of Nanga Parbat)",
        "forest_type": "Coniferous Forest bordering high-altitude alpine meadow",
        "covered_area": "Localized valley forest and meadow belt (not precisely documented)",
        "history_origin": (
            "A traditional summer grazing meadow (Rama Lake sits above the tree line) used seasonally by local "
            "herding communities; it has become a gateway trekking base on the Astore side of Nanga Parbat."
        ),
        "wildlife_nature": (
            "Pine forest gives way to open alpine meadow and Rama Lake near the treeline, with views of Nanga "
            "Parbat (8,126 m); habitat for markhor and a range of high-altitude birdlife in the surrounding hills."
        ),
        "attractions_recreation": (
            "Camping among pine forest below Nanga Parbat, jeep tracks and short hikes to Rama Lake, and access "
            "to further trekking toward Nanga Parbat base camp."
        ),
    },
    "Kalam Forest": {
        "location": "Kalam Valley, Upper Swat District, Khyber Pakhtunkhwa (also referred to as part of Ushu Forest)",
        "forest_type": "Coniferous Forest",
        "covered_area": "Forms a continuous belt with Ushu Forest stretching toward Utror and Matiltan",
        "history_origin": (
            "One of Swat's best-known forest tracts, historically part of the princely State of Swat's managed "
            "timber reserves before merger into Pakistan in 1969; now a cornerstone of upper Swat's tourism economy."
        ),
        "wildlife_nature": (
            "Pine, deodar and fir cover with diverse wildlife; the forest and adjoining Swat River corridor "
            "support trout streams and seasonal wildflower meadows."
        ),
        "attractions_recreation": (
            "Gateway to Mahodand Lake, Usho and Matiltan valleys; popular for hiking, riverside picnicking, "
            "trout fishing and camping, especially May–October."
        ),
    },
    "Chitral Forests": {
        "location": "Chitral District, Khyber Pakhtunkhwa (including Chitral Gol, Birir and other side valleys)",
        "forest_type": "Coniferous / dry temperate forest",
        "covered_area": "Distributed across multiple valleys; Chitral Gol National Park alone covers 7,750 hectares",
        "history_origin": (
            "Long managed under the former princely State of Chitral's forest and hunting reserves, including "
            "royal hunting grounds later converted into protected areas after Chitral's accession to Pakistan."
        ),
        "wildlife_nature": (
            "Deodar, chilgoza pine and oak forest across steep, dry-temperate terrain; famous as prime habitat "
            "for the flare-horned (Kashmir) markhor, snow leopard, and diverse high-altitude birdlife."
        ),
        "attractions_recreation": (
            "Wildlife viewing (especially markhor) in Chitral Gol National Park, trekking in side valleys such "
            "as Birir (home to the Kalash community), and access to the wider Hindu Kush trekking region."
        ),
    },
    "Margalla Hills Scrub Forests": {
        "location": "Margalla Hills, Islamabad Capital Territory",
        "forest_type": "Sub-tropical broadleaf / scrub forest transitioning to moist temperate forest at higher points",
        "covered_area": "Part of Margalla Hills National Park's 17,386 hectares",
        "history_origin": (
            "Foothill scrub and mixed broadleaf forest at the edge of the Himalayan and Potohar zones, protected "
            "since Margalla Hills National Park's establishment in 1980 to conserve its unique Sino-Himalayan flora and fauna."
        ),
        "wildlife_nature": (
            "Phulai (Acacia modesta), olive and other scrub species lower down give way to pine and oak at "
            "higher elevations; habitat for the grey goral, barking deer, common leopard and rich birdlife at "
            "the western edge of many Himalayan species' ranges."
        ),
        "attractions_recreation": (
            "Islamabad's most-used hiking network (Trail 3, 5, 6 and others), Daman-e-Koh and Pir Sohawa "
            "viewpoints, and close access to the Shakarparian and Rawal Lake green belt."
        ),
    },
}

# ---------------------------------------------------------------------------
# 15. NATIONAL PARKS & MAJOR RECREATIONAL PARKS
# ---------------------------------------------------------------------------
# Note: not every entry below is an IUCN/provincially-notified "national park" —
# several (e.g. city/cantonment parks in Multan and Lahore) are large municipal
# recreational parks that are commonly referred to as such locally. This is
# flagged per-entry via the "type" field.
NATIONAL_PARKS = {
    "Ayub National Park": {
        "province": "Punjab", "type": "National Park",
        "area": "About 4 sq mi (2,300 acres), one of Pakistan's smallest national parks",
        "established": "1959, by President Ayub Khan",
        "notes": "Located in Rawalpindi; features an artificial lake, a miniature train, and extensive gardens; was under Rawalpindi Cantonment Board management from 1959–2001.",
    },
    "Jallo Park, Lahore": {
        "province": "Punjab", "type": "Recreation & Wildlife Park",
        "area": "461 acres (187 hectares)",
        "established": "1978",
        "notes": "About 7 km east of Lahore; one of Lahore's three main wildlife parks (with Changa Manga and Lahore Zoo Safari); includes a Wildlife Breeding Centre, a large boating/fishing lake, and a Botanical Garden & Butterfly House.",
    },
    "Lulusar-Dudipatsar National Park": {
        "province": "Khyber Pakhtunkhwa", "type": "National Park",
        "area": "About 560 km² (together with adjacent Saiful Muluk National Park, the pair protect ~88,000 hectares)",
        "established": "2003",
        "notes": "Upper Kaghan Valley, Mansehra District; protects the alpine Lulusar Lake (source of the Kunhar River) and Dudipatsar Lake amid snow-capped peaks; habitat for snow leopard and black bear.",
    },
    "Lal Suhanra National Park": {
        "province": "Punjab", "type": "National Park",
        "area": "About 658 km² (162,500 acres)",
        "established": "1972 — Pakistan's first and oldest national park",
        "notes": "At the edge of the Cholistan Desert, ~35 km from Bahawalpur; a UNESCO Biosphere Reserve combining desert, irrigated forest plantation and the Patisar Lake wetland; reintroduction site for blackbuck and chinkara.",
    },
    "Kirthar National Park": {
        "province": "Sindh", "type": "National Park",
        "area": "About 3,087 km² — Pakistan's third-largest national park",
        "established": "1974 (initially a wildlife sanctuary from 1972)",
        "notes": "Spans the Kirthar Range across Jamshoro and Dadu districts; the first Pakistani park listed on the UN's 1975 List of National Parks; protects Sindh ibex, urial, chinkara and leopard.",
    },
    "Khunjerab National Park": {
        "province": "Gilgit-Baltistan", "type": "National Park",
        "area": "226,913 hectares",
        "established": "1975, on the recommendation of zoologist Dr George Schaller",
        "notes": "High-altitude park (over half above 4,000 m) along the Karakoram Highway to the Khunjerab Pass; established chiefly to protect the Marco Polo sheep, alongside snow leopard and Himalayan ibex.",
    },
    "City Park, Multan": {
        "province": "Punjab", "type": "Municipal Recreational Park",
        "area": "Not precisely documented",
        "established": "Not precisely documented",
        "notes": "A public recreational park within Multan city offering green space, walking areas and family facilities.",
    },
    "Kashmir Park, DHA Multan": {
        "province": "Punjab", "type": "Municipal / Community Park",
        "area": "Not precisely documented",
        "established": "Not precisely documented",
        "notes": "A community park within the DHA Multan housing development, used for local recreation and walking.",
    },
    "Chitral Gol National Park": {
        "province": "Khyber Pakhtunkhwa", "type": "National Park",
        "area": "7,750 hectares",
        "established": "1984",
        "notes": "Lower Chitral District beside the Chitral River, about two hours from Chitral town; one of the most important refuges for the flare-horned (Kashmir) markhor.",
    },
    "Chaman Zar-e-Askari Park, Multan": {
        "province": "Punjab", "type": "Cantonment Recreational Park",
        "area": "Not precisely documented",
        "established": "Not precisely documented",
        "notes": "A garrison/cantonment-run recreational park in Multan (the name translates roughly to \"Garden of the Soldiers\"), used for public leisure.",
    },
    "Jinnah Park": {
        "province": "Multiple provinces (several cities have a Jinnah Park, e.g. Islamabad, Faisalabad)", "type": "Municipal Recreational Park",
        "area": "Varies by city",
        "established": "Varies by city",
        "notes": "A common name for municipal parks across Pakistan named after Quaid-e-Azam Muhammad Ali Jinnah; typically offer walking tracks, playgrounds and green space.",
    },
    "Hingol National Park": {
        "province": "Balochistan", "type": "National Park",
        "area": "About 6,100 km² (610,043 acres) — Pakistan's largest national park",
        "established": "1988",
        "notes": "Spans Lasbela, Awaran and Gwadar districts along the Makran Coastal Highway; famous for the Hingol mud volcanoes, the wind-sculpted 'Princess of Hope' rock formation, and habitat for Sindh ibex and Balochistan black bear.",
    },
    "Shakarparian National Park": {
        "province": "Islamabad Capital Territory", "type": "Urban Park / Cultural Complex",
        "area": "Part of the wider Islamabad Wildlife Management Board green belt alongside Margalla Hills and Rawal Lake",
        "established": "Developed alongside Islamabad's planning from the 1960s onward",
        "notes": "Hilltop park in Islamabad hosting the Pakistan Monument, Lok Virsa heritage museum and the Shakarparian Hills viewpoint overlooking the capital.",
    },
    "Faisal Park, Mumtazabad": {
        "province": "Punjab", "type": "Municipal Recreational Park",
        "area": "Not precisely documented",
        "established": "Not precisely documented",
        "notes": "A neighborhood recreational park in the Mumtazabad area of Multan.",
    },
    "Pir Lasura National Park": {
        "province": "Azad Jammu & Kashmir", "type": "National Park",
        "area": "About 1,580 hectares (15.8 km²) per peer-reviewed ecological studies (a government gazette figure of 2,916 acres for specified forest compartments is also cited)",
        "established": "2005",
        "notes": "Kotli District, near the Line of Control; subtropical pine and scrub forest habitat for common leopard, Indian pangolin and three vulture species including the Himalayan griffon.",
    },
    "Hazarganji-Chiltan National Park": {
        "province": "Balochistan", "type": "National Park",
        "area": "15,555 hectares (some sources cite a larger historical extent of ~325,000 acres)",
        "established": "1980",
        "notes": "Mastung District near Quetta, between the Hazarganji and Chiltan mountain ranges; established to protect the critically endangered, Pakistan-endemic Chiltan markhor.",
    },
    "Pakistan Park": {
        "province": "Punjab", "type": "Municipal Recreational Park",
        "area": "Not precisely documented",
        "established": "Not precisely documented",
        "notes": "A municipal recreational park name used in several Pakistani cities for public green space and family recreation.",
    },
    "Machiara National Park": {
        "province": "Azad Jammu & Kashmir", "type": "National Park",
        "area": "13,532 hectares",
        "established": "1996",
        "notes": "Muzaffarabad District; established chiefly to protect the western tragopan pheasant; infrastructure was damaged in the 2005 Kashmir earthquake.",
    },
    "Rajana Forest / Bhagat Wildlife Park": {
        "province": "Punjab", "type": "Wildlife Breeding Centre / Park",
        "area": "About 15 acres",
        "established": "1987–89",
        "notes": "On the Rajana–Samundri road, about 17 km from Toba Tek Singh and 3 km from Rajana town; a Punjab Wildlife & Parks Department breeding centre and recreational forest park.",
    },
    "Margalla Hills National Park": {
        "province": "Islamabad Capital Territory", "type": "National Park",
        "area": "17,386 hectares",
        "established": "1980",
        "notes": "Foothills bordering Islamabad; drained by the Kurang River, rich in Sino-Himalayan flora and fauna including grey goral, barking deer and leopard; one of the most-visited national parks in the world by hiking traffic.",
    },
}

# ---------------------------------------------------------------------------
# 16. PCA (COURT OF ARBITRATION) TIMELINE — Indus Waters Western Rivers
#     Arbitration (Islamic Republic of Pakistan v. Republic of India),
#     PCA Case No. 2023-01
# ---------------------------------------------------------------------------
PCA_TIMELINE = [
    {"date": "19 Aug 2016", "event": "Pakistan institutes arbitration", "detail": "Pakistan files a Request for Arbitration under Annexure G of the Indus Waters Treaty over the design of India's Kishenganga and Ratle hydropower projects; a Court of Arbitration is constituted, with the PCA acting as Secretariat."},
    {"date": "21 Dec 2022", "event": "India writes to the World Bank on the Neutral Expert track", "detail": "India pursues a parallel Neutral Expert process for the same technical questions, a procedural divergence that becomes a recurring point of contention."},
    {"date": "3 Feb 2023", "event": "PCA press release on expedited competence procedure", "detail": "The Court concludes its first meeting and initiates an expedited procedure to decide its own competence after India objects to the arbitration proceeding at all."},
    {"date": "6 Jul 2023", "event": "Award on the Competence of the Court", "detail": "The Court unanimously rejects India's objections and confirms it is competent to hear Pakistan's claims."},
    {"date": "18 Sep 2023", "event": "Corrections to the Award on Competence", "detail": "Minor corrections issued to the July 2023 competence award."},
    {"date": "22 Mar 2024", "event": "Pakistan files its Memorial (First Phase on the Merits)", "detail": "Pakistan submits its detailed written case on the technical design disputes."},
    {"date": "Apr 2024", "event": "Site visit to the Neelum-Jhelum Hydro-Electric Plant", "detail": "The Court conducts a site visit under an agreed protocol as part of its fact-finding on run-of-river design questions."},
    {"date": "7 Jan 2025", "event": "Neutral Expert issues competence decision", "detail": "In the parallel track, the Neutral Expert finds India's referred points of difference fall within the scope of the treaty's technical Annexure F."},
    {"date": "Apr 2025", "event": "India announces the IWT is 'held in abeyance'", "detail": "Following a deadly attack on civilians in Indian-administered Kashmir, India states it will hold the treaty in abeyance pending action against cross-border terrorism — the first such disruption in the treaty's history."},
    {"date": "16 May 2025", "event": "Procedural Order No. 15 issued", "detail": "The Court invites both parties' written submissions on whether India's abeyance announcement affects the Court's and the Neutral Expert's competence; only Pakistan files a submission."},
    {"date": "27 Jun 2025", "event": "Supplemental Award on the Competence of the Court", "detail": "The Court finds the treaty makes no provision for unilateral abeyance and reaffirms its continuing jurisdiction to proceed with the case."},
    {"date": "8 Aug 2025", "event": "Award on Issues of General Interpretation of the IWT", "detail": "The Court rules on a set of general treaty-interpretation questions underlying the Kishenganga/Ratle/Pakal Dul design disputes."},
    {"date": "8 Nov 2025", "event": "Decision on Pakistan's Request for Clarification", "detail": "The Court issues a clarification of aspects of its August 2025 interpretation award, in response to a Pakistani request."},
    {"date": "21 Nov 2025", "event": "Procedural Order No. 17 (Second Phase on the Merits)", "detail": "The Court sets the schedule for the next substantive phase of the case, addressing the specific technical designs of the disputed projects."},
    {"date": "12 Mar 2026", "event": "Procedural Order No. 21", "detail": "The Court addresses interim measures and the present status of the treaty in light of India's continued abeyance position."},
]

HEAD_MARALA_NOTE = (
    "The dashboard records reported concerns about reduced Chenab flows at Head Marala and potential "
    "consequences for irrigation and crops as stakeholder claims, rather than asserting a causal crop-loss "
    "estimate without a hydrological dataset."
)
