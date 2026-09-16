from .state import Faction

FACTION_DEFINITIONS = {
    "eastern_woodlands": {
        "name": "Eastern Woodlands Society",
        "population": 100, "food": 70, "wealth": 35, "military": 35,
        "stability": 75, "diplomacy": 45,
        "territory": ["Atlantic Woodlands"],
        "objectives": ["Maintain population", "Preserve autonomy", "Reach wealth 75"],
    },
    "pueblo": {
        "name": "Pueblo Society",
        "population": 85, "food": 65, "wealth": 30, "military": 40,
        "stability": 80, "diplomacy": 35,
        "territory": ["Southwest"],
        "objectives": ["Protect agriculture", "Preserve population", "Maintain autonomy"],
    },
    "mississippian": {
        "name": "Mississippian Successor Society",
        "population": 110, "food": 80, "wealth": 40, "military": 35,
        "stability": 65, "diplomacy": 50,
        "territory": ["Mississippi Valley"],
        "objectives": ["Maintain stability", "Dominate regional trade", "Preserve independence"],
    },
    "haudenosaunee": {
        "name": "Haudenosaunee",
        "population": 95, "food": 75, "wealth": 40, "military": 40,
        "stability": 75, "diplomacy": 60,
        "territory": ["Northeastern Woodlands"],
        "objectives": ["Preserve autonomy", "Build diplomacy", "Maintain population"],
    },
}

def create_factions():
    factions = {}
    for key, data in FACTION_DEFINITIONS.items():
        factions[key] = Faction(key=key, **data)
    return factions

def choose_faction(factions):
    items = list(factions.items())
    print("\nChoose your society:\n")
    for i, (_, f) in enumerate(items, 1):
        print(f"{i}. {f.name}")
        print(f"   Population {f.population:.0f} | Food {f.food:.0f} | "
              f"Wealth {f.wealth:.0f} | Military {f.military:.0f} | "
              f"Stability {f.stability:.0f} | Diplomacy {f.diplomacy:.0f}")
        print(f"   Goal: {f.objectives[0]}")
    while True:
        raw = input("\n> ").strip()
        try:
            n = int(raw)
            if 1 <= n <= len(items):
                return items[n - 1][0]
        except ValueError:
            pass
        print("Enter a number from the list.")
