"""
Some Web sites impose certain rules for passwords. 
Write a function that checks whether a string is a valid password. 
Suppose the password rules are as follows:
•	A password must have at least eight characters.
•	A password must consist of only letters and digits and no spaces.
•	A password must contain at least two digits.

Write a program that prompts the user to enter a password and displays valid
password if the rules are followed or invalid password otherwise.

Input			output
Mario1		invalid
Mariochahoud12	valid
Mario12		invalid
Mario 12		invalid 

"""

def validPass(password):
    if len(password) < 8:
        return False
    if not password.isalnum():
        return False
    if sum([1 for c in password if c.isdigit()]) < 2:
        return False
    return True

password = input("Enter a password: ")
if validPass(password):
    print("valid")
else:
    print("invalid")
