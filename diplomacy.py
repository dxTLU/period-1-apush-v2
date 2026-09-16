def relationship_label(value):
    if value >= 75: return "Allied"
    if value >= 25: return "Friendly"
    if value > -25: return "Neutral"
    if value > -75: return "Hostile"
    return "At War"

def initialize_relationships(state):
    keys = list(state.factions)
    for key in keys:
        f = state.factions[key]
        for other in keys:
            if other != key:
                f.relationships.setdefault(other, 0)

def change_relationship(state, source_key, target_key, amount):
    source = state.factions[source_key]
    target = state.factions[target_key]
    source.relationships[target_key] = max(-100, min(100, source.relationships.get(target_key, 0) + amount))
    target.relationships[source_key] = max(-100, min(100, target.relationships.get(source_key, 0) + amount / 2))

def diplomacy_menu(state):
    f = state.player
    others = [x for k, x in state.factions.items() if k != f.key]
    if not others:
        return
    print("\nDiplomatic relations:")
    for other in others:
        print(f"- {other.name}: {relationship_label(f.relationships.get(other.key, 0))} "
              f"({f.relationships.get(other.key, 0):+.0f})")
