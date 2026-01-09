# flip7-scorer

Minimal MVP for a Streamlit-based scorer app for the Flip7 game.

## Quick features

- Scorer page: add player names (default 3), add players, start game
- Round inputs: input scores per player per round, click "Next round" to commit
- Running totals with conditional color scale (white → dark green)
- Advisor page: placeholder for future analytics

## Quickstart

Install requirements and run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Tests & CI

- Unit tests with pytest are under `tests/`
- GitHub Actions workflow runs tests on push/PR to `main`

See `README_APP.md` for Windows-friendly running instructions.

