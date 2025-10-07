# 🪢 Hangman Game (Python Console Edition)

A classic word-guessing game built in Python for the terminal. Players try to guess a randomly selected word one letter at a time. With every incorrect guess, the hangman gets closer to being fully drawn. You have 6 lives — use them wisely!

---

## 🎮 Gameplay Overview

- The game randomly selects a word from a predefined word list.
- Players guess one letter at a time.
- Incorrect guesses reduce the number of lives.
- The game ends when:
  - The word is fully guessed ✅
  - The player runs out of lives ❌

---

## 🖼️ Features

- ✅ ASCII art hangman stages
- ✅ A fun splash screen/logo at the start
- ✅ Word masking with underscores (`_ _ _`) to represent hidden letters
- ✅ Feedback for repeated guesses
- ✅ Warning messages showing remaining lives
- ✅ Clean modular structure using multiple Python files

---

## 🧱 File Structure

hangman/
│
├── main.py # Main game logic
├── hangman_words.py # Word list used in the game
├── hangman_art.py # ASCII art for logo and hangman stages
└── README.md # Project documentation

---

## ▶️ How to Run the Game

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/hangman.git
   cd hangman
