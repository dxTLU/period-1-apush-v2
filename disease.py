import random
from .state import clamp

def disease_risk(exposure):
    if exposure < 10: return "LOW"
    if exposure < 30: return "MODERATE"
    if exposure < 60: return "HIGH"
    if exposure < 80: return "SEVERE"
    return "CATASTROPHIC"

def annual_disease_check(faction, contact_pressure=0):
    if contact_pressure:
        faction.disease_exposure = clamp(
            faction.disease_exposure + contact_pressure * 0.25
        )
    risk = disease_risk(faction.disease_exposure)
    chance = faction.disease_exposure / 500
    if random.random() < chance:
        severity = {
            "LOW": 0.01, "MODERATE": 0.02, "HIGH": 0.04,
            "SEVERE": 0.07, "CATASTROPHIC": 0.12
        }[risk]
        loss = faction.population * severity
        faction.population = max(1, faction.population - loss)
        faction.stability = clamp(faction.stability - severity * 70)
        return loss, risk
    return 0, risk
