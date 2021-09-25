"""
Problem 5
Write a program that asks the user to enter his/her first name and age number separated by space. Then print the following: 
Hi, my name and I am age years old.
I will be in x years, 90 years old.

Input

Enter your name and age (separated by a space): Simon 21

Output

Hi, my name is Simon and I am 21 years old
I will be in 69 years, 90 years old. 
"""

# get the user firstname and age
first_name , age = input("Enter your first name and age separated by a space: ").split(" ")

#calculate the years till the user becomes 90
years_till_ninety = 90 - int(age)

# output the result to the screen
print(f"Hi, my name is {first_name} and I am {age} years old\nI will be in {years_till_ninety}, 90 years old")

