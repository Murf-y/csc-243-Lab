"""
Problem 3
Write a program that reads a value representing a number of seconds. Print the equivalent amount of time in hours, minutes and seconds.
"""

# Get the seconds from the user
seconds = int(input("Enter the number of seconds: "))

# Calculate hours , minutes and seconds use integer division and remainder.
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60

# Output the result to the terminal use formating
print("{} seconds is {} hours, {} minutes and {} seconds.".format(seconds, hours, minutes, seconds))

"""
Explanation:
lets say seconds was 3665

seconds =3665
hours = seconds // 3600 = 3665 // 3600 = 1
seconds = seconds % 3600 = 3665 % 3600 = 565
minutes = seconds // 60 = 565 // 60 = 1
seconds = seconds % 60 = 565 % 60 = 5

thats is why hours is 1 , minutes is 1 and seconds is 5 when the input is 3665
"""