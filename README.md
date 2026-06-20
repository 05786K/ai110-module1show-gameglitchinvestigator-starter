# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Instead of a screenshot, here is a textual walkthrough that steps through a sample game in order. (Difficulty: **Normal** — range 1–50, 8 attempts. For this run the secret number is **37**, visible in the "Developer Debug Info" expander.)

1. The app loads on Normal difficulty and shows the prompt: *"Guess a number between 1 and 50. Attempts left: 8."* The secret (37) stays fixed across clicks instead of resetting on every Submit.
2. User enters a guess of **20** and clicks "Submit Guess 🚀" → game returns the hint **"📈 Go HIGHER!"** (20 is below 37). Attempts left drops to 7, and the hint stays on screen instead of vanishing on the next rerun.
3. User enters **45** → game returns **"📉 Go LOWER!"** (45 is above 37). Attempts left drops to 6. The history in Debug Info now reads `[20, 45]`.
4. User enters **abc** (invalid) → game shows *"That is not a number."* and **does not** burn an attempt — attempts left stays at 6. An out-of-range guess like **75** is likewise rejected with *"Enter a number between 1 and 50."*
5. User enters **37** → game shows balloons 🎈 and *"You won! The secret was 37."* The score updates correctly after each guess, the status switches to **won**, and Submit is locked until "New Game 🔁" resets the secret, attempts, score, and history for a fresh round.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
