from dataclasses import dataclass, field
from typing import Dict, List, Optional


def clamp(value: float, low: float = 0, high: float = 100) -> float:
    return max(low, min(high, value))


@dataclass
class Faction:
    key: str
    name: str
    population: float
    food: float
    wealth: float
    military: float
    stability: float
    diplomacy: float
    european_influence: float = 0
    disease_exposure: float = 0
    territory: List[str] = field(default_factory=list)
    objectives: List[str] = field(default_factory=list)
    relationships: Dict[str, float] = field(default_factory=dict)
    flags: Dict[str, bool] = field(default_factory=dict)

    def adjust(self, **changes):
        for attr, amount in changes.items():
            if not hasattr(self, attr):
                raise AttributeError(f"Unknown faction attribute: {attr}")
            value = getattr(self, attr) + amount
            if attr not in {"population", "food", "wealth", "military", "stability",
                            "diplomacy", "european_influence", "disease_exposure"}:
                setattr(self, attr, value)
            elif attr == "population":
                setattr(self, attr, max(1, value))
            else:
                setattr(self, attr, clamp(value))


@dataclass
class GameState:
    current_year: int = 1491
    end_year: int = 1520
    player_key: Optional[str] = None
    factions: Dict[str, Faction] = field(default_factory=dict)
    completed_events: List[str] = field(default_factory=list)
    decisions_made: List[str] = field(default_factory=list)
    history_log: List[str] = field(default_factory=list)
    apush_score: int = 0
    running: bool = True

    @property
    def player(self) -> Faction:
        if self.player_key is None or self.player_key not in self.factions:
            raise RuntimeError("No player faction selected.")
        return self.factions[self.player_key]

    def log(self, message: str):
        self.history_log.append(f"{self.current_year}: {message}")
