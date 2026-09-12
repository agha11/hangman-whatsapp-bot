import os
import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "development-secret-key-change-me")

# Word banks by difficulty
WORD_BANKS = {
    "easy": [
        "apple", "house", "tiger", "water", "phone",
        "green", "music", "happy", "train", "school"
    ],
    "medium": [
        "python", "flask", "developer", "hangman", "website",
        "computer", "journey", "puzzle", "diamond", "football"
    ],
    "hard": [
        "algorithm", "javascript", "cybersecurity", "entrepreneur",
        "architecture", "blockchain", "programming", "development",
        "automation", "technology"
    ],
}

LIVES_BY_DIFFICULTY = {
    "easy": 8,
    "medium": 6,
    "hard": 5,
}


def init_game(difficulty=None):
    difficulty = difficulty or session.get("difficulty", "medium")
    if difficulty not in WORD_BANKS:
        difficulty = "medium"

    session["difficulty"] = difficulty
    session["word"] = random.choice(WORD_BANKS[difficulty]).lower()
    session["guessed"] = []
    session["lives"] = LIVES_BY_DIFFICULTY[difficulty]
    session["game_over"] = False
    session["won"] = False


def get_game_state():
    word = session.get("word", "")
    guessed = session.get("guessed", [])
    lives = session.get("lives", 0)
    max_lives = LIVES_BY_DIFFICULTY.get(session.get("difficulty", "medium"), 6)

    display_word = [
        letter if letter in guessed else "_"
        for letter in word
    ]

    won = bool(word) and all(letter in guessed for letter in word)
    game_over = lives <= 0 or won

    session["won"] = won
    session["game_over"] = game_over

    mistakes = max_lives - lives
    return {
        "word": word,
        "guessed": guessed,
        "lives": lives,
        "max_lives": max_lives,
        "mistakes": mistakes,
        "display_word": display_word,
        "won": won,
        "game_over": game_over,
        "difficulty": session.get("difficulty", "medium"),
        "score": session.get("score", 0),
        "games_won": session.get("games_won", 0),
        "games_played": session.get("games_played", 0),
    }


@app.route("/")
def index():
    if "word" not in session:
        init_game()

    return render_template("index.html", **get_game_state())


@app.route("/guess", methods=["POST"])
def guess():
    if "word" not in session:
        init_game()

    if session.get("game_over", False):
        return redirect(url_for("index"))

    letter = request.form.get("letter", "").lower().strip()

    if len(letter) == 1 and letter.isalpha():
        guessed = session.get("guessed", [])

        if letter not in guessed:
            guessed.append(letter)
            session["guessed"] = guessed

            if letter not in session.get("word", ""):
                session["lives"] = max(0, session.get("lives", 0) - 1)

    state = get_game_state()

    # Award points only once when a game is completed.
    if state["game_over"] and state["won"] and not session.get("result_counted", False):
        difficulty_bonus = {"easy": 50, "medium": 100, "hard": 175}[state["difficulty"]]
        session["score"] = session.get("score", 0) + difficulty_bonus + (state["lives"] * 10)
        session["games_won"] = session.get("games_won", 0) + 1
        session["games_played"] = session.get("games_played", 0) + 1
        session["result_counted"] = True
    elif state["game_over"] and not state["won"] and not session.get("result_counted", False):
        session["games_played"] = session.get("games_played", 0) + 1
        session["result_counted"] = True

    return redirect(url_for("index"))


@app.route("/reset")
def reset():
    init_game(session.get("difficulty", "medium"))
    session["result_counted"] = False
    return redirect(url_for("index"))


@app.route("/difficulty", methods=["POST"])
def difficulty():
    selected = request.form.get("difficulty", "medium").lower()
    if selected not in WORD_BANKS:
        selected = "medium"

    init_game(selected)
    session["result_counted"] = False
    return redirect(url_for("index"))


@app.route("/reset-score")
def reset_score():
    session["score"] = 0
    session["games_won"] = 0
    session["games_played"] = 0
    init_game(session.get("difficulty", "medium"))
    session["result_counted"] = False
    return redirect(url_for("index"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
