"""
Problem 4:
Write a function that generate a List of random numbers. 
Your function should take 3 arguments and return a List:
			def genList( Len, Low, Upp):
				# Len for length of the list, 
				#Low for the lower bound , Upp for the upper bound of the numbers

Write a program that includes the an implementation of the genList , linearSearch and binarySearch Functions. 
Your program should:
•	Generate a list of random numbers. (Use a very large value for Len)
•	Prompt the user to enter a Value. (This should be done for several values)
•	Search for the entered value using both search functions measuring the time it takes for each function.
•	Output the results.
"""

import random
import time
def genList( Len, Low, Upp):
    return [random.randint(Low, Upp) for _ in range(Len)]
def linear_search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return i
    return -1
def binary_search(L, e):
    start = 0
    end = len(L) - 1
    while start <= end:
        mid = (start + end) // 2
        if L[mid] == e:
            return mid
        elif L[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def main():
    Len = 10**6
    Low = 1
    Upp = 10**6
    L = genList(Len, Low, Upp)
    e = int(input("Enter a number: "))

    start = time.time()
    linear_search(L, e)
    end = time.time()
    print(f"Linear search took: {end - start:.2F} seconds")

    L.sort()
    start = time.time()
    binary_search(L, e)
    end = time.time()
    print(f"Binary search took: {end - start:.2F} seconds")

    try_again = input("Try again? (y/n): ")
    if try_again == "y":
        main()
    

if __name__ == "__main__":
    main()