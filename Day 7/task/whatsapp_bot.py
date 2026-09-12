import random
import nltk
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Download NLTK words
nltk.download('words', quiet=True)
from nltk.corpus import words

app = Flask(__name__)

# Game state per user
games = {}

# Word list (4 to 8 letters)
word_list = [w.lower() for w in words.words() if 4 <= len(w) <= 8 and w.isalpha()]

# Hangman ASCII Art stages (from 6 lives down to 0)
STAGES = [
    """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========
""",
    """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========
""",
    """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========
""",
    """
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
""",
    """
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
""",
    """
   +---+
   |   |
   O   |
       |
       |
       |
=========
""",
    """
   +---+
   |   |
       |
       |
       |
       |
=========
"""
]


@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    user_number = request.values.get('From', '')
    user_message = request.values.get('Body', '').strip().lower()

    resp = MessagingResponse()
    reply = resp.message()

    # Start a new game
    if user_message == "start" or user_number not in games:
        word = random.choice(word_list)
        games[user_number] = {
            "word": word,
            "guesses": [],
            "lives": 6
        }
        display = " ".join(["_" for _ in word])
        stage_art = STAGES[6]

        reply.body(
            f"🎮 *Welcome to Hangman!*\n\n"
            f"Word length: *{len(word)} letters*\n"
            f"💡 *Hint:* Starts with *'{word[0].upper()}'*\n\n"
            f"```\n{stage_art}\n```\n"
            f"Word: `{display}`\n"
            f"Lives left: 6\n\n"
            f"Send a single letter to guess, type *hint* for help, or *start* for a new game."
        )
        return str(resp)

    game = games[user_number]

    # Handle explicit hint request
    if user_message == "hint":
        first_letter = game["word"][0].upper()
        last_letter = game["word"][-1].upper()
        reply.body(f"💡 *Hint:* The word starts with *'{first_letter}'* and ends with *'{last_letter}'*.")
        return str(resp)

    # Input validation
    if len(user_message) != 1 or not user_message.isalpha():
        reply.body("Please send a single letter (A-Z) or type *hint*.")
        return str(resp)

    guess = user_message

    if guess in game["guesses"]:
        reply.body(f"You already guessed '{guess}'. Try a different letter!")
        return str(resp)

    game["guesses"].append(guess)

    if guess not in game["word"]:
        game["lives"] -= 1

    display = " ".join([letter if letter in game["guesses"] else "_" for letter in game["word"]])
    stage_art = STAGES[game["lives"]]

    if game["lives"] <= 0:
        reply.body(
            f"```\n{stage_art}\n```\n"
            f"❌ *Game Over!* The word was *{game['word'].upper()}*.\n"
            f"Type *start* to play again."
        )
        del games[user_number]
    elif "_" not in display:
        reply.body(f"🎉 *You Win!* You guessed *{game['word'].upper()}*!\nType *start* to play again.")
        del games[user_number]
    else:
        status_msg = (
            f"```\n{stage_art}\n```\n"
            f"Word ({len(game['word'])} letters): `{display}`\n"
            f"Lives left: {game['lives']}\n"
            f"Guessed: {', '.join(game['guesses'])}"
        )
        if guess not in game["word"]:
            status_msg = f"Wrong guess! '{guess}' is not in the word.\n\n" + status_msg
        reply.body(status_msg)

    return str(resp)


if __name__ == "__main__":
    app.run(port=5000)