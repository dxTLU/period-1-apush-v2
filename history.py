TIMELINE = {
    1491: "Indigenous societies across North America are diverse in political organization, economy, and culture.",
    1492: "Columbus reaches the Caribbean.",
    1493: "The second Spanish voyage begins sustained colonization in the Caribbean.",
    1494: "Treaty of Tordesillas divides Spanish and Portuguese overseas spheres.",
    1497: "John Cabot sails for England.",
    1500: "Pedro Álvares Cabral reaches Brazil for Portugal.",
    1510: "Spanish colonization expands in the Caribbean and mainland exploration intensifies.",
    1512: "Laws of Burgos regulate aspects of Spanish colonial labor and Indigenous treatment.",
    1513: "Balboa reaches the Pacific; Ponce de León explores Florida.",
    1517: "Luther's Ninety-Five Theses mark a major phase of the Protestant Reformation.",
    1519: "Cortés enters the Mexica sphere; Magellan's expedition begins.",
    1520: "Smallpox spreads through central Mexico."
}

def show_timeline():
    print("\nHistorical timeline:")
    for year, text in TIMELINE.items():
        print(f"{year}: {text}")

def campaign_report(state):
    f = state.player
    historical_years = sorted(TIMELINE)
    print("\n" + "=" * 60)
    print("CAMPAIGN REPORT")
    print("=" * 60)
    print(f"Society: {f.name}")
    print(f"Final year: {state.current_year}")
    print(f"Population: {f.population:.1f}")
    print(f"Food: {f.food:.1f}")
    print(f"Wealth: {f.wealth:.1f}")
    print(f"Military: {f.military:.1f}")
    print(f"Stability: {f.stability:.1f}")
    print(f"Diplomacy: {f.diplomacy:.1f}")
    print(f"European influence: {f.european_influence:.1f}")
    print(f"Disease exposure: {f.disease_exposure:.1f}")
    print(f"APUSH questions correct: {state.apush_score}")
    print("\nHistorical reference:")
    for year in historical_years:
        if year <= state.end_year:
            print(f"- {year}: {TIMELINE[year]}")
    print("\nRecent campaign log:")
    for entry in state.history_log[-10:]:
        print(f"- {entry}")
