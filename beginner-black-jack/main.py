from art import logo
import random
import subprocess as sp

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(cards):
    score = sum(cards)

    # this becouse the 11 can be 1 or 11
    while score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)

    return score


def clear_screen():
    sp.call('clear', shell=True)


def compare(user_score, computer_score):

    if computer_score == 21:
        return "Lose, opponent has Blackjack 😱"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score == user_score:
        return "Draw 🙃"
    elif user_score == 21:
        return "Win with a Blackjack 😎"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score and user_score <= 21:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    clear_screen()
    print(logo)

    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]

    game_continue = True

    while game_continue:
        user_score = calculate_score(user_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        while calculate_score(user_cards) < 21:
            user_choice = input(
                "Type 'y' to get another card, type 'n' to pass: ")

            if user_choice == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(
                    f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")
            else:
                break

        while calculate_score(computer_cards) < 17:
            computer_cards.append(deal_card())

        final_user_score = calculate_score(user_cards)
        final_computer_score = calculate_score(computer_cards)

        print(
            f"Your final hand: {user_cards}, final score: {final_user_score}")

        print(
            f"Computer's final hand: {computer_cards}, final score: {final_computer_score}")

        print(compare(final_user_score, final_computer_score))

        is_want_play = input(
            "Do you want to play a game of Blackjack? Type 'y' or 'n': ")

        if is_want_play == 'y':
            play_game()
        else:
            print("Goodbye")
            exit()


play_game()
