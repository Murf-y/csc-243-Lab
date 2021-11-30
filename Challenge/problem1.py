"""
Write a program that prompts the user to input a year and determine whether the year is a
leap year or not.
Leap Years are any year that can be evenly divided by 4. A year that is evenly divisible by 100 is
a leap year only if it is also evenly divisible by 400. 
"""
def readInt(prompt):
    num = input(prompt)
    while not num.isnumeric():
        print("Please enter a number.")
        num = input(prompt)
    return int(num)

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def main():
    year = readInt("Enter a year: ")
    if is_leap(year):
        print(year, "is a Leap year.")
    else:
        print(year, "is not a Leap year.")

main()