"""
Problem 2
Write a program that generate a random uppercase alphabetic character and asks the user to guess on the generated character by entering an uppercase alphabetic character.
The program should check if the entered character is the same as the generated one, if they are equal print the Good Guess else print Wrong Guess.

Sample Runs:
Enter an uppercase alphabetic character: A
Wrong Guess
The Random character is: B 

Enter an uppercase alphabetic character: C
Good Guess
The Random character is: C 
"""

import random
def random_uppercase_char():
    """
    Generate a random int between 65 and 90 inclusive
    then transform it to its corresponding character base on the ascii table
    
    return type -> string
    """
    return chr(random.randint(65, 90))

user_guess = input("Enter an uppercase alphabetic character: ")
random_char = random_uppercase_char()
user_guess.strip()
if random_char == user_guess:
    print("Good Guess")
else:
    print("Wrong Guess")
print("The Random character is: ",random_char)


"""
Sample:

Enter an uppercase alphabetic character: A
Good Guess
The Random character is:  A
"""