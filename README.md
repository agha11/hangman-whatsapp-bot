# Hangman Arena

A mobile-friendly Hangman game built with Python, Flask and Gunicorn.

## Features

- Easy / Medium / Hard difficulty
- Responsive mobile layout
- On-screen A-Z keyboard
- Physical keyboard support
- SVG Hangman drawing
- Score and win counter
- New game / reset score
- Session-based game state
- Render-ready Gunicorn start command

## Render

Build Command:
`pip install -r requirements.txt`

Start Command:
`gunicorn app:app`

Environment variable:
`SECRET_KEY` = a long random secret value

## Local

```bash
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000
