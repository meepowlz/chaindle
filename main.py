# Chaindle
"""
Todo:
- Distinguish between number of letters
    (ex. if there is only one A, guesses with multiple As will only highlight one)
- Distinguish between guesses prior to correct position
    (ex. if a user guesses a AGAPE for SHAME, only the second A should highlight
"""
import random

word_list = ["apple", "tacos", "words", "games", "water"]


def select_word():
    index = random.randint(0, len(word_list) - 1)
    word = word_list[index]
    word_split = []
    print(index)
    print(word)
    for i, letter in enumerate(word):
        print(letter)
        char_split = {
            letter: 1
        }
        word_split.append(char_split)
    return word


def check_word(user_guess, answer):
    if user_guess == answer:
        print("You guessed the word correctly!")
        return True
    else:
        for i, letter in enumerate(user_guess):
            if letter in answer:
                if letter == answer[i]:
                    print(f"{letter} is in the right spot")
                else:
                    print(f"{letter} is in the word")
        return False


def main():
    user_win = False
    answer = select_word()
    while not user_win:
        user_guess = input("Make a guess").lower()
        user_win = check_word(user_guess, answer)


main()

