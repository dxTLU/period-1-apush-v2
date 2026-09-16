from .state import clamp

def process_economy(faction):
    # Abstract annual production/consumption for the MVP.
    food_gain = max(2, faction.population * 0.08)
    food_cost = faction.population * 0.055
    faction.food = clamp(faction.food + food_gain - food_cost)
    if faction.food < 15:
        faction.stability = clamp(faction.stability - 6)
        faction.population = max(1, faction.population - faction.population * 0.02)
    else:
        faction.stability = clamp(faction.stability + 1)
    faction.wealth = clamp(faction.wealth + max(0, faction.food - 45) * 0.025)
    return faction
