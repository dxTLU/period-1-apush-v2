from dataclasses import dataclass
from typing import Callable, List

from .state import GameState


@dataclass
class Decision:
    key: str
    title: str
    description: str
    choices: List[tuple]


def apply_effects(faction, effects):
    faction.adjust(**effects)


def available_decisions(state: GameState):
    f = state.player
    decisions = [
        Decision(
            "invest_agriculture", "Invest in agriculture",
            "Redirect labor toward food production.",
            [
                ("Expand cultivation", {"food": 10, "stability": 2, "wealth": -5}),
                ("Keep resources diversified", {"food": 4, "wealth": 2}),
            ],
        ),
        Decision(
            "strengthen_diplomacy", "Strengthen diplomacy",
            "Invest time and resources in alliances and exchange.",
            [
                ("Host a diplomatic gathering", {"diplomacy": 10, "wealth": -4}),
                ("Send envoys", {"diplomacy": 6, "wealth": -1}),
            ],
        ),
        Decision(
            "prepare_defense", "Prepare defenses",
            "Increase military readiness at an economic cost.",
            [
                ("Mobilize warriors", {"military": 10, "food": -5, "stability": -2}),
                ("Fortify settlements", {"military": 6, "wealth": -4, "stability": 2}),
            ],
        ),
    ]
    if f.european_influence >= 10:
        decisions.append(Decision(
            "manage_contact", "Manage European contact",
            "Choose how your society responds to growing European presence.",
            [
                ("Encourage controlled exchange", {"wealth": 8, "european_influence": 4,
                                                   "disease_exposure": 5, "diplomacy": 3}),
                ("Restrict contact", {"stability": 4, "diplomacy": -2, "european_influence": -3}),
            ],
        ))
    return decisions


def choose_decision(state: GameState):
    decisions = available_decisions(state)
    print("\nAvailable decisions:")
    for i, d in enumerate(decisions, 1):
        print(f"{i}. {d.title} — {d.description}")
        for j, (name, _) in enumerate(d.choices, 1):
            print(f"   {j}) {name}")
    while True:
        raw = input("\nDecision number (or ENTER to skip): ").strip()
        if raw == "":
            return None
        try:
            n = int(raw)
            if 1 <= n <= len(decisions):
                d = decisions[n - 1]
                while True:
                    c = input(f"Choice for '{d.title}': ").strip()
                    try:
                        ci = int(c)
                        if 1 <= ci <= len(d.choices):
                            name, effects = d.choices[ci - 1]
                            apply_effects(state.player, effects)
                            state.decisions_made.append(f"{d.key}:{ci}")
                            state.log(f"Decision: {d.title} — {name}.")
                            return d
                    except ValueError:
                        pass
                    print("Enter a valid choice number.")
        except ValueError:
            pass
        print("Enter a valid decision number.")
