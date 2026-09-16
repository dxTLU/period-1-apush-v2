from game.factions import create_factions

def test_factions_exist():
    factions = create_factions()
    assert len(factions) == 4
    assert factions["pueblo"].population == 85

def test_faction_adjustment_clamps():
    f = factions = create_factions()["pueblo"]
    f.adjust(food=-1000)
    assert f.food == 0
