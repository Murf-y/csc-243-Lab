"""
Hangman Game:  Write a program that prompts the user to guess a word.
The program starts by displaying dashes for each character in the word. 
Then, the user starts by inputting characters. 
If the character is in the word, it replaces the dash and the program proceeds. 
The user is allowed a number of attempts equal to double the length of the word. 
Hint: Store the words in a list and then have the program pick one randomly. 

"""

import random

def validateLetter(message):
    # (str) -> str
    while True:
        letter = input(message)
        if len(letter) != 1:
            print("You should input a single letter")
        elif not letter.isalpha():
            print("It is not an ASCII lowercase letter")
        else:
            return letter.lower()
def main():
    # (None) -> None

    words = ["python", "java", "kotlin", "javascript", "cpp", "c", "html", "css", "php", "typescript", "dart"]
    chosen_word = random.choice(words)
    print()
    print("_______________")
    print("H A N G M A N")
    print("_______________")
    print(f"You have {len(chosen_word) * 2} attempts to guess what programmin languages it is!")
    print("-" * len(chosen_word))
    attempts = 0
    letters_to_guess = [i for i in chosen_word]
    right_guessed_letters = {}
    while attempts < len(chosen_word) * 2:
        letter = validateLetter("Input a letter: ")
        if letter in letters_to_guess:
            letter_index = letters_to_guess.index(letter)
            for i in range(letters_to_guess.count(letter)):
                letters_to_guess.remove(letter)
            right_guessed_letters[letter] = letter_index
            
        else:
            attempts += 1
            print("No such letter in the word\n")
            print(f"Attempts left: {len(chosen_word) * 2 - attempts}\n")
        
        print("".join(map(lambda x: x if x in right_guessed_letters else "_", chosen_word)))

        if attempts >= len(chosen_word) * 2:
            print("You are hanged!")
            print(f"The word was: {chosen_word}")
            print("_______________")
            break
        
        if not letters_to_guess:
            print("You guessed the word!")
            print("You survived!")
            print("_______________")
            break

if __name__ == "__main__":
    main()

"""Sample run

_______________
H A N G M A N
_______________
You have 6 attempts to guess what programmin languages it is!
---
Input a letter: c
c__
Input a letter: p
No such letter in the word

Attempts left: 5

c__
Input a letter: s
css
You guessed the word!
You survived!
_______________
"""
