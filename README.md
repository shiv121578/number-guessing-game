# Number Guessing Game

A beginner-friendly **Python project** where the user tries to guess a randomly generated number between 1 and 100. The game gives helpful **range-based hints** and rewards the player with **points** based on how quickly they guess the number.

---

## Features

-  Random number generation (1 to 100)
- Feedback: "Too high" / "Too low"
- Smart hints:
  - After 1st wrong guess → range of 20 numbers
  - After 2nd → range of 10 numbers
  - After 3rd → range of 5 numbers
- Scoring system:
  | Attempt | Points |
  |---------|--------|
  | 1st     | 100    |
  | 2nd     | 50     |
  | 3rd     | 25     |
  | 4th     | 10     |
  | 5th     | 5      |
  | 6+      | 0      |

-  Clean console interface
-  Input validation for non-numeric guesses

---

##  How to Run

1. Make sure you have Python 3 installed.
2. Download the file `number_guessing.py`.
3. Open your terminal or command prompt and run:
   ```bash
   python number_guessing.py
