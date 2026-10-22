# Habit Tracker

A small Pixela API exercise for managing a daily habit graph.

## Requirements

- Python 3
- A Pixela username and user token

Install dependencies with `pip install -r requirements.txt`. Set `PIXELA_USERNAME`
and `PIXELA_TOKEN` in your shell before running `python main.py`. A sample
configuration is provided in `.env.example`; the script does not load `.env`
automatically, so export the values through your shell or your preferred local
environment manager. Keep real credentials private.

The example's delete request is disabled by default. Set
`DELETE_YESTERDAY_PIXEL=true` only when you intentionally want to delete the
previous day's graph entry.