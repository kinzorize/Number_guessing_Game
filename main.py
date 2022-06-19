from random import randint
from art import logo
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def check_answer(answer, guess, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it, the answer was {answer}")


def set_difficulty():
    level = input("Choose the difficulty 'Easy' or 'Hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN


def game():
    print(logo)
    print("Welcome to the guessing game! ")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        # Let the user guess the number
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(answer, guess, turns)
        if turns == 0:
            print("You ran out of guesses, you lose")
            return
        elif guess != answer:
            print("guess again please!")


game()
