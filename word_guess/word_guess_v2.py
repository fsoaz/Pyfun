# A function to call the name, age, and sex of the user
# Tests the inputs
# Age has to be an integer
# The sex has to be female or male, no other options
# View player info before start de game

import random


def get_user_info():
    while True:
        name = input("Enter your name: ").lower().strip()
        if name:
            break
        else:
            print("Name cannot be empty. Please try again")

    while True:
        age_input = input("Enter your age: ")
        try:
            age = int(age_input)
            break
        except ValueError:
            print("Age must be an integer. Please try again")

    while True:
        sex = input("Enter your sex: ").strip().lower()
        if sex in ("male", "m"):
            sex = "Male"
            break
        elif sex in ("female", "f"):
            sex = "Female"
            break
        else:
            print("Sex must be male or female")

    print(f"Player info: {name}, Age: {age}, Sex: {sex}")
    return name, age, sex

def choose_word():
    words = ["python", "github", "claude", "chatgpt", "programming", "algorithm"]
    return random.choice(words)

def display_progress(word, guessed_letters):
    progress = ""
    for letter in word:
        if letter in guessed_letters:
            progress += letter + " "
        else:
            progress += "_ "
    return progress.strip()

def get_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").lower().strip()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter!")
            else:
                return guess
        else:
            print("Please enter a single alphabetic character.")

def play_game():
    name, age, sex = get_user_info()
    secret_word = choose_word()
    guessed_letters = []
    print("Let's start the game!")

    while True:
        print(display_progress(secret_word, guessed_letters))
        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if all(letter in guessed_letters for letter in set(secret_word)):
            print(f"Congratulations {name}! You guessed the word: {secret_word}")
            break
    
    play_again = input("\nPlay another game? (y/n): ").lower().strip()
    if play_again not in ('y', 'yes'):
        print("Thanks for playing!")
        return

if __name__ == "__main__":
    play_game()