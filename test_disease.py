from game.disease import disease_risk

def test_disease_risk():
    assert disease_risk(0) == "LOW"
    assert disease_risk(50) == "HIGH"
    assert disease_risk(100) == "CATASTROPHIC"
