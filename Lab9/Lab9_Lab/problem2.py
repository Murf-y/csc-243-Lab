"""
Design and write a complete Application program that ask the user to enter an integer N and simulates the roll two dies N times (N being a large number such 10000 times). Your program should count and output the number and percentage of occurrences of each 

•	Implement and use a function roll that simulate the rolling of a Die:
Def roll():
   # () -> int
   # returns a random number between 1 and 6

•	Include in the application a prompt for re-running the simulation.

"""

import random
from collections import Counter

def readInt(prompt):
    num = input(prompt)
    while not num.isnumeric():
        num = input(f"Enter a valid integer, Try again, {prompt}")
    return int(num)

def roll():
    # () -> int
    return random.randint(1,6)
def main():
    n = readInt("Enter number of rolls: ")
    numbers_rolled = []
    for _ in range(n):
        numbers_rolled.append(roll())
    numbers_occurrences = Counter(numbers_rolled)
    numbers_occurrences = sorted(numbers_occurrences.items())
    for number, occurrences in numbers_occurrences:
         print(f"{number}: {occurrences} ({occurrences/n*100:.2f}%)")
    again = input("Again? (y/n): ")
    if again == "y":
        main()
    

if __name__ == "__main__":
    main()

"""
Sample runs

Enter number of rolls: 100000
1: 16559 (16.56%)
2: 16655 (16.66%)
3: 16688 (16.69%)
4: 16793 (16.79%)
5: 16646 (16.65%)
6: 16659 (16.66%)
Again? (y/n): n
"""