# APUSH Period 1 — The New World

A playable text-based historical strategy simulator covering 1491–1520.

## Features

- Four initial playable Indigenous societies
- Annual strategy loop from 1491 through 1520
- Food, wealth, population, military, stability, diplomacy, European influence, and disease exposure
- Historical events tied to APUSH Period 1 themes
- Columbian Exchange and epidemic-disease mechanics
- Player decisions with consequences
- Diplomacy and relationship tracking
- APUSH knowledge checks with explanations
- Historical timeline and campaign report
- Save/load support
- Automated tests

## Run

Requires Python 3.10 or newer.

```bash
python main.py
```

## Test

Install pytest if necessary:

```bash
python -m pip install pytest
```

Then:

```bash
pytest
```

## Notes

The numerical systems are intentionally abstract. They are designed to create a playable educational simulation rather than reproduce precise demographic or economic estimates.

The game begins with Indigenous societies because Period 1 starts in 1491. European actors and more detailed colonial political systems are planned as the next expansion.

## Suggested next expansion

1. Add Spain as a playable faction after 1492.
2. Add a Mexica-centered event chain with Indigenous allies and rivals.
3. Add Spanish internal factions: Crown, colonists, missionaries, and merchants.
4. Add England, France, and Portugal as AI actors.
5. Add trade routes and resource-specific Columbian Exchange effects.
6. Add more APUSH questions for causation, comparison, continuity/change, and contextualization.
7. Add a browser UI after the rules engine is stable.
