import random


def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    while True:
        try:
            # Ask the user for their guess
            user_guess = int(input("Please enter your guess: "))

            # Check if the guess is within the valid range
            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Provide hints based on the user's guess
            if user_guess < number_to_guess:
                print("Too low! Try a higher number.")
            elif user_guess > number_to_guess:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the correct number: {number_to_guess}")
                break  # Exit the loop when the correct number is guessed

        except ValueError:
            # Handle the case where the input is not a number
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    guess_the_number()
