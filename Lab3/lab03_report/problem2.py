"""
Problem 2
Write a program that reads an integer value which is always five digits and prints it in reverse leaving 2 spaces between them.
Input
45632
Output
2  3  6  5  4
"""

# first methode "bruteforce => does not work if number is not 5 digits" O(1)
number = input("Enter a 5 digit number: ")
print("{0} {1:2d} {2:2d} {3:2d} {4:2d}".format(int(number[4]), int(number[3]), int(number[2]), int(number[1]), int(number[0])))

# second methode "dynamic"  O(1)
number = input("Enter a 5 digit number: ")
print("  ".join(number[::-1]))


