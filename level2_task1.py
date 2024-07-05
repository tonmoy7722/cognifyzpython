import random


def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    guessing_game()
