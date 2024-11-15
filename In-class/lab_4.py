import random
# Generate a random number between 10 and 50
target_number = random.randint(10, 50)
tries = 0
guessed_correctly = False

print("Guess the number between 10 and 50!")

# Loop
while not guessed_correctly:
    try:
        # User's guess
        guess = int(input("Enter your guess: "))
        tries += 1

        # Check the guess
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number {target_number} correctly.")
            print(f"It took you {tries} tries.")
    except ValueError:
        print("Please enter a valid integer.")
