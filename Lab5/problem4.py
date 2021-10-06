"""
Problem 4
Ask the user to enter as many integers as he/she like, separated by spaces, store the numbers in a list. Use list functions and methods to print the list, the number of integers, entered, the sum, the largest, the smallest and how many zeros the list contain.
Input:
Enter as many numbers as you like, separated by spaces: 42 34 0 56 1 3 0
Output: 
Your entered: [42, 34, 0, 56, 1, 3, 0]
Your list contains 7 numbers
Sum:136
Smallest:0
Largest: 56
Your List contains 2 zeros

"""

numbers = input("Enter as many number as you like, seperated by spaces: ")
numbers = numbers.split()
numbers = map(int, numbers)
numbers = list(numbers)
print("Your entered:", numbers)
print("Your list contains", len(numbers), "numbers")
print("Sum:", sum(numbers))
print("Smallest:", min(numbers))
print("Largest:", max(numbers))
print("Your list contains", numbers.count(0), "zeros")


"""
output:
Enter as many number as you like, seperated by spaces: 1 10 12 1230 10
Your entered: [1, 10, 12, 1230, 10]
Your list contains 5 numbers
Sum: 1263
Smallest: 1
Largest: 1230
Your list contains 0 zeros
"""