"""
Problem 4
Write a function that takes as arguments two positive integers, finds and returns their greatest common divisor. 
Write a program to invoke and test the functions on several pairs of numbers. 
"""

def gcd(a, b):
    """
    (int,int) => int
    find greatest common divisor for two numbers
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(10, 5))
print(gcd(10, 125))
print(gcd(125,25,25))
print(gcd(12,4))