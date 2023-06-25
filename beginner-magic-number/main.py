import random
from art import logo


def welcome_message():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return 10
    else:
        return 5


def make_guess(random_number, attempts):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_number = int(input("Make a guess: "))
        attempts -= 1
        difference = user_number - random_number

        if user_number == random_number:
            return f"You got it! The answer was {random_number}."
        elif abs(difference) <= 0.4 * random_number:
            closer = round((1 - abs(difference) / random_number) * 100, 2)
            print(f"You are {closer}% close.")
        elif user_number > random_number:
            print("Too high.")
        elif user_number < random_number:
            print("Too low.")

        if attempts > 0:
            print("Guess again.")
    return f"You've run out of guesses, you lose. The number was {random_number}."


def game():
    welcome_message()
    random_number = random.randint(1, 100)
    attempts = set_difficulty()
    message = make_guess(random_number, attempts)
    print(message)


game()
