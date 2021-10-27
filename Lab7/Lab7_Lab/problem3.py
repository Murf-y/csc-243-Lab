"""
Problem 3

Using functions in your implementation, write an Eggy-peggy program that reads a string from the user and converts it
 to a new string by placing egg in front of every vowel (aA, eE,iI,oO,uU).
For example, the string Python becomes Pytheggon.
Sample Output 
Enter your message: I LOVE YOU 
The Encrypted message is: eggI LeggOVeggE YeggOeggU
"""

def encrypt(message):
    """
    Encrypts a message by placing an egg in front of every vowel.
    """
    vowels = "aeiouAEIOU"
    encrypted = ""
    for char in message:
        if char in vowels:
            encrypted += "egg" + char
        else:
            encrypted += char
    return encrypted

message = input("Enter your message: ")
print("The Encrypted message is:", encrypt(message))
