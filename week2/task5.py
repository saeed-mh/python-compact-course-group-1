events = {
    "Mini E-Bus Parcours": "19.09.2026",
    "Pido – das Maskottchen von DEW21": "19.09.2026",
    "Kreativ-Station Glühbirnen": "19.09.2026",
    "Hüpfburg": "19.09.2026",
    "Mittelalterliche Mitmach-Musik": "19.09.2026",
    "Sieh an, sieh an! Mode vergangener Zeiten": "19.09.2026",
    "Bogenschießen für Kinder": "19.09.2026",
    "Fiurfaro – Feuershow": "19.09.2026",
    "Fußball-Spielstationen zum Mitmachen!": "19.09.2026",
    "Walk-Act DFM-Maskottchen RIO": "19.09.2026"
}

museum_night = "19.09.2026"

for event, date in events.items():
    if date == museum_night:
        print(event, "-", date)