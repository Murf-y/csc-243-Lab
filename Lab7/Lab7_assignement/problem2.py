"""
Problem 2

Using functions in your implementation, write a program that reads integers directly
 from the user place them in a list, print the list, then removes duplicate elements in it and prints it out again. 
"""

def readInt():
    """
    Reads an integer from the user and returns it.
    """
    num = input("Enter an integer or 0 to stop: ")
    while not num.isnumeric():
        num = input("Enter an integer or 0 to stop: ")
    return int(num)

num = readInt()
num_list = []
while num != 0:
    num_list.append(num)
    num = readInt()
print(num_list)
num_list_modified = [i for i in num_list if num_list.count(i) == 1]
print(num_list_modified)
