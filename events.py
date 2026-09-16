from .decisions import apply_effects
from .state import clamp

EVENTS = [
    {
        "key": "columbus_1492", "year": 1492, "title": "Columbus Reaches the Caribbean",
        "description": "European transatlantic contact begins a new phase of exchange, competition, and disease transmission.",
        "effects": {"european_influence": 12, "disease_exposure": 7},
        "apush": "Period 1: European exploration initiated sustained contact between the Americas, Europe, and Africa."
    },
    {
        "key": "second_voyage_1493", "year": 1493, "title": "A Larger Spanish Expedition",
        "description": "Spain expands Caribbean colonization and establishes a more durable European presence.",
        "effects": {"european_influence": 8, "disease_exposure": 5},
        "apush": "European colonization combined settlement, extraction, conversion, and competition for imperial claims."
    },
    {
        "key": "tordesillas_1494", "year": 1494, "title": "Treaty of Tordesillas",
        "description": "Spain and Portugal divide overseas spheres of influence through a papal-backed agreement.",
        "effects": {"diplomacy": 2, "european_influence": 3},
        "apush": "European powers used diplomacy and religious authority to structure imperial competition."
    },
    {
        "key": "cabots_1497", "year": 1497, "title": "Cabot's Voyage",
        "description": "English exploration strengthens European interest in the North Atlantic.",
        "effects": {"european_influence": 3},
        "apush": "European states competed for routes, resources, and territorial claims in the Atlantic."
    },
    {
        "key": "portugal_brazil_1500", "year": 1500, "title": "Portuguese Brazil",
        "description": "Portuguese activity in Brazil expands the Atlantic imperial system.",
        "effects": {"european_influence": 5, "disease_exposure": 3},
        "apush": "The Atlantic world connected imperial expansion with labor, trade, and biological exchange."
    },
    {
        "key": "laws_burgos_1512", "year": 1512, "title": "Laws of Burgos",
        "description": "The Spanish Crown issues regulations concerning Indigenous labor and treatment.",
        "effects": {"european_influence": 3, "stability": -1},
        "apush": "Spanish colonial rule generated debates over Indigenous rights, labor, conversion, and imperial authority."
    },
    {
        "key": "balboa_1513", "year": 1513, "title": "Balboa Reaches the Pacific",
        "description": "Spanish exploration reveals the scale of the Pacific and increases strategic interest in the Americas.",
        "effects": {"european_influence": 5},
        "apush": "Exploration expanded European geographic knowledge and imperial ambitions."
    },
    {
        "key": "reformation_1517", "year": 1517, "title": "The Protestant Reformation",
        "description": "Religious conflict in Europe begins reshaping the political context of later Atlantic competition.",
        "effects": {"diplomacy": -1},
        "apush": "European religious divisions influenced state power, migration, and later colonization."
    },
    {
        "key": "cortes_1519", "year": 1519, "title": "Cortés Enters Mexico",
        "description": "Spanish forces enter the Mexica sphere and encounter a complex political landscape.",
        "effects": {"european_influence": 8, "disease_exposure": 8},
        "apush": "Spanish conquest depended on Indigenous alliances and political divisions as well as European military advantages."
    },
    {
        "key": "smallpox_1520", "year": 1520, "title": "Smallpox Epidemic in Central Mexico",
        "description": "Smallpox spreads in central Mexico, causing catastrophic mortality among populations without prior exposure.",
        "effects": {"disease_exposure": 30, "population": -18, "stability": -12},
        "apush": "The Columbian Exchange included pathogens that caused severe demographic consequences in the Americas."
    },
]

def events_for_year(year):
    return [e for e in EVENTS if e["year"] == year]

def trigger_event(state, event):
    f = state.player
    print("\n" + "=" * 60)
    print(f"HISTORICAL EVENT: {event['title']}")
    print(event["description"])
    effects = dict(event.get("effects", {}))
    # The 1520 population effect is percentage-like in the data.
    if event["key"] == "smallpox_1520":
        effects["population"] = -f.population * 0.18
    apply_effects(f, effects)
    state.completed_events.append(event["key"])
    state.log(f"Event: {event['title']}.")
    print("\nEffects:")
    for k, v in effects.items():
        print(f"  {k.replace('_', ' ').title()}: {v:+.1f}")
    print(f"\nAPUSH connection: {event['apush']}")
    input("\nPress ENTER to continue...")
