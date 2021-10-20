"""
Problem 3
Write a program that randomly generates an integer between 0 and 100, inclusive.
 The program prompts the user to enter a number continuously until the number matches the randomly generated number.
  For each user input, the program tells the user whether the input is too low or too high,
   so the user can choose the next input intelligently and should record the number of trials before the user enters 
   the correct guess.

Here is a sample run: 
The random guess is 50.
Input	Output
90	Too High (1)
45	Too Low (2)
52	Too High (3)
50	With 4 attempts, you got it !
 
"""
import random

random_num = random.randint(0, 100)

def readInt():
    num = input("Enter a number between 0 and 100: ")
    while not num.isnumeric() or int(num) <0 or int(num)>100:
        num = input("Enter a valid integer between 0 and 100 please: ")
    return int(num)
guess = readInt()

count = 0
while guess != random_num:
    count += 1
    if guess < random_num:
        print("Too Low")
        
    else:
        print("Too High")
    guess = readInt()
print(f"With {count} attempts, you got it !")
        