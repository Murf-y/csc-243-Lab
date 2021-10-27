"""
Problem 1

Create a function that takes two lists having the same length as parameters and then does the multiplication of the two lists and return it.

Original list 1 : [1, 3, 4, 6, 8]
Original list 2 : [4, 5, 6, 2, 10]
Resultant list is : [4, 15, 24, 12, 80]
Write a program to read two lists invoke the function and print the results.

"""
def multiply_list(list_a, list_b):
    # (list,list) => list
    return [a*b for a,b in zip(list_a, list_b)]

list_a = [1, 3, 4, 6, 8]
list_b = [4, 5, 6, 2, 10]
print(multiply_list(list_a, list_b))