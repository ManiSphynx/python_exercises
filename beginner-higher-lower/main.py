import random
from art import logo, vs
from game_data import data


def get_random_celebrity():
    return random.choice(data)


def print_celebrity(letter, celebrity):
    print(
        f"Compare {letter}: {celebrity['name']}, a {celebrity['description']}, from {celebrity['country']}")


def give_hint(celebrity_a, celebrity_b):
    if celebrity_a['follower_count'] > celebrity_b['follower_count']:
        print(f"Hint: {celebrity_a['name']} has more followers")
    else:
        print(f"Hint: {celebrity_b['name']} has more followers")


def get_most_popular_celebrity(celebrity_a, celebrity_b):
    return 'a' if celebrity_a['follower_count'] > celebrity_b['follower_count'] else 'b'


def score_and_hint_option(score):
    if score > 1:
        return f"Current score: {score}. You can type 'H' for a hint."
    return f"Current score: {score}."


def get_user_input(score):
    print(score_and_hint_option(score))
    return input("Who has more followers? Type 'A' or 'B': ").lower()


def update_score(answer, correct_answer, score):
    if answer == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}.\n")
    else:
        print(f"Sorry, that's wrong. Current score: {score}")
        print(f"The correct answer was {correct_answer}")
        score = max(0, score - 1)
    return score


def play_game():
    print(logo)
    score = 0
    continue_game = True

    while continue_game:
        celebrity_a = get_random_celebrity()
        celebrity_b = get_random_celebrity()

        print_celebrity('A', celebrity_a)
        print(vs)
        print_celebrity('B', celebrity_b)

        answer = get_user_input(score)

        if score > 1 and answer == 'h':
            give_hint(celebrity_a, celebrity_b)
            score -= 1
            continue

        correct_answer = get_most_popular_celebrity(celebrity_a, celebrity_b)
        score = update_score(answer, correct_answer, score)

        if score == 0 and answer != correct_answer:
            print("You lose all your points!")
            continue_game = False


play_game()
