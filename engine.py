from .state import GameState
from .factions import create_factions, choose_faction
from .decisions import choose_decision
from .events import events_for_year, trigger_event
from .economy import process_economy
from .disease import annual_disease_check
from .diplomacy import initialize_relationships, diplomacy_menu
from .history import show_timeline, campaign_report
from .apush import ask_question
from .save_load import save_game, load_game, SAVE_PATH

class Game:
    def __init__(self, state=None):
        self.state = state or GameState()
        if not self.state.factions:
            self.state.factions = create_factions()
        initialize_relationships(self.state)

    def start(self):
        print("=" * 60)
        print("APUSH PERIOD 1 — THE NEW WORLD")
        print("Historical Strategy Simulator, 1491–1520")
        print("=" * 60)
        if self.state.player_key is None:
            self.state.player_key = choose_faction(self.state.factions)
        print(f"\nYou are playing as: {self.state.player.name}")
        print("Type HELP at any prompt to see commands.")
        input("\nPress ENTER to begin...")
        self.run()

    def show_status(self):
        f = self.state.player
        print("\n" + "-" * 60)
        print(f"YEAR {self.state.current_year} | {f.name}")
        print("-" * 60)
        for label, attr in [
            ("Population", "population"), ("Food", "food"), ("Wealth", "wealth"),
            ("Military", "military"), ("Stability", "stability"),
            ("Diplomacy", "diplomacy"), ("European Influence", "european_influence"),
            ("Disease Exposure", "disease_exposure")
        ]:
            print(f"{label:<22} {getattr(f, attr):6.1f}")

    def command(self, raw):
        cmd = raw.strip().lower()
        if cmd == "status":
            self.show_status(); return True
        if cmd == "diplomacy":
            diplomacy_menu(self.state); return True
        if cmd == "history":
            show_timeline(); return True
        if cmd == "save":
            save_game(self.state); return True
        if cmd == "load":
            if not SAVE_PATH.exists():
                print("No save file found."); return True
            self.state = load_game(); initialize_relationships(self.state)
            print("Game loaded."); return True
        if cmd == "help":
            print("\nCommands: STATUS, DIPLOMACY, HISTORY, SAVE, LOAD, HELP, QUIT")
            return True
        if cmd == "quit":
            self.state.running = False; return False
        return None

    def turn(self):
        self.show_status()
        print("\nYour yearly decision:")
        choose_decision(self.state)

        for event in events_for_year(self.state.current_year):
            if event["key"] not in self.state.completed_events:
                trigger_event(self.state, event)

        process_economy(self.state.player)
        loss, risk = annual_disease_check(
            self.state.player,
            contact_pressure=self.state.player.european_influence * 0.10
        )
        if loss > 0:
            print(f"\nDisease event: approximately {loss:.1f} population lost. Risk level: {risk}.")
            self.state.log(f"Disease outbreak; population loss {loss:.1f}.")
        if self.state.current_year in {1492, 1500, 1512, 1519}:
            ask_question(self.state, self.state.current_year)

        self.state.current_year += 1

    def run(self):
        while self.state.running and self.state.current_year <= self.state.end_year:
            self.turn()
            if self.state.current_year <= self.state.end_year:
                raw = input("\nPress ENTER for the next year, or enter a command: ").strip()
                if raw:
                    result = self.command(raw)
                    if result is False:
                        break
        if self.state.running:
            campaign_report(self.state)
