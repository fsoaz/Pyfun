#First game project - Word Guess

import random

def choose_word():
    words = ["Python", "GitHub", "Claude", "ChatGPT", "Programming", "God"]
    return random.choice(words)

def display_progress(word, guessed_letters):
    progress = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            progress += letter + " "
        else:
            progress += "_ "
    return progress.strip()
    
def check_letter(letter, word):
    if letter in word:
        print('That\'s correct')
    else:
        print('Sorry, that letter is not in the word.')
    

def get_guess():
    # Ask the player for a single letter
    guess = input("Enter a letter: ").lower().strip()
    return guess


def check_guess(word, guess, guessed_letters):
   guess = guess.lower()
   if guess in guessed_letters:
        return "You already guessed that letter!"
   else:
       guessed_letters.append(guess) #add the new guess
       if guess in word.lower():
           return f"Good job! '{guess}' is in the word."
       else:
           return f"Sorry, '{guess}' is not in the word."

def play_game():
    print("Word Guess Game - Edition 1")

    secret_word = choose_word()   # choose once
    guessed_letters = []          # start empty

    while True:
        # 1 - the current progress
        print(display_progress(secret_word, guessed_letters))

        # 2 - ask player for a guess
        guess = get_guess()

        # 3 - check the guess and print the result
        message = check_guess(secret_word, guess, guessed_letters)
        print(message)

        # 4 - check if the word is complete
        if all(letter.lower() in guessed_letters for letter in secret_word):
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

if __name__ == "__main__": 
    play_game()