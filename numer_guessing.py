import random

# Generate the secret number
secret_number = random.randint(1, 100)
attempts = 0

# Scoring based on attempt number
score_table = {1: 100, 2: 50, 3: 25, 4: 10, 5: 5}

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Guess the number! Fewer attempts = more points.")

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess == secret_number:
        # Get score based on attempts
        score = score_table.get(attempts, 0)
        print(f"Correct! You guessed it in {attempts} attempts.")
        print(f" Your Score: {score} points")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    # Provide helpful hints based on attempt number
    if attempts == 1:
        start = max(1, secret_number - 10)
        end = min(100, secret_number + 9)
        print(f" Hint: The number is between {start} and {end}.")
    elif attempts == 2:
        start = max(1, secret_number - 5)
        end = min(100, secret_number + 4)
        print(f"Hint: The number is between {start} and {end}.")
    elif attempts == 3:
        start = max(1, secret_number - 2)
        end = min(100, secret_number + 2)
        print(f"Hint: The number is between {start} and {end}.")
