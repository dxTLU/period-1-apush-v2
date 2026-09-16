from game.factions import create_factions
from game.decisions import apply_effects

def test_apply_effects():
    f = create_factions()["pueblo"]
    old = f.wealth
    apply_effects(f, {"wealth": 5})
    assert f.wealth == old + 5
