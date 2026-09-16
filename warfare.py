import random

def resolve_battle(attacker_strength, defender_strength, terrain_bonus=0,
                   alliance_bonus=0, technology_bonus=0, surprise=0):
    attacker = attacker_strength + terrain_bonus + alliance_bonus + technology_bonus + surprise
    defender = defender_strength + terrain_bonus
    attacker_roll = attacker * random.uniform(0.85, 1.15)
    defender_roll = defender * random.uniform(0.85, 1.15)
    if attacker_roll > defender_roll * 1.05:
        return "attacker"
    if defender_roll > attacker_roll * 1.05:
        return "defender"
    return "draw"
