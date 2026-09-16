import json
from dataclasses import asdict
from pathlib import Path

SAVE_PATH = Path("savegame.json")

def save_game(state, path=SAVE_PATH):
    data = asdict(state)
    data["player_key"] = state.player_key
    Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Game saved to {path}")

def load_game(path=SAVE_PATH):
    from .state import GameState, Faction
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    factions = {k: Faction(**v) for k, v in data["factions"].items()}
    state = GameState(
        current_year=data["current_year"], end_year=data["end_year"],
        player_key=data["player_key"], factions=factions,
        completed_events=data["completed_events"],
        decisions_made=data["decisions_made"],
        history_log=data["history_log"],
        apush_score=data["apush_score"], running=data.get("running", True)
    )
    return state
