# flip-seven-scorer

Source code for my FlipSeven browser & advisor app.

## Features

### Scorer Page
- Add player names (default 4) and start game
- Input scores per player per round
- Click "Next round" to commit and advance
- Running totals with conditional color scale to show the leader

### Advisor Page
- Enter your drawn cards and cards of other players
- Get strategic recommendations (HIT or STAND)
- View current score and expected value calculations
- See bust chance and event card probabilities
- Detailed breakdown of expected values for each remaining card in the deck

## Quickstart

Install requirements and run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure

```
flip7-scorer/
├── app.py                      # Main Streamlit app entry point
├── flip7_scorer/
│   ├── core/
│   │   ├── scoring.py          # Score tracking logic
│   │   ├── advisor_logic.py    # Advisor calculations and recommendations
│   │   └── default_fields.py   # Default game settings
│   └── pages/
│       ├── scorer.py           # Scorer page UI
│       └── advisor.py          # Advisor page UI
```

## Notes

- The Advisor's F3 (Flip 3) calculator is not yet implemented

