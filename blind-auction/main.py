import subprocess as sp
from art import logo


def clear_screen():
    sp.call('clear', shell=True)


def get_user_input(prompt):
    return input(prompt)


def add_bid(name, bid, bids):
    bids[name] = bid


def get_highest_bid(bids):
    return max(bids, key=bids.get)


def print_winner(winner, bid):
    print(
        f"The winner is {winner} with a bid of ${bid}")


def secret_auction():
    print("Welcome to the secret auction program.")
    bids = {}

    while True:
        user_name = get_user_input("What is your name?: ")
        user_bid = int(get_user_input("What's your bid?: $"))
        add_bid(user_name, user_bid, bids)

        user_choice = get_user_input(
            "Are there any other bidders? Type 'yes' or 'no'.\n").lower()

        if user_choice == "yes":
            clear_screen()
        elif user_choice == "no":
            winner = get_highest_bid(bids)
            print_winner(winner, bids[winner])
            print(logo)
            break


secret_auction()
