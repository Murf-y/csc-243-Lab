"""
Problem 3
A triangle is considered valid if the sum of each 2 sides is greater than the remaining third side. Also, triangles can be classified as follows:
•	Equilateral: If all sides are equal
•	Isosceles: If 2 sides are equal
•	Scalene: If all sides are not equal
Write a program that takes the length of three sides and print “equilateral”, “isosceles”, or “scalene”. If the input does not create a valid triangle print “invalid”.

Sample Input	Sample Output
3 2 3           isosceles
2 5 1	        invalid
"""
def classify_triangle(side_a,side_b,side_c):
    """
    classify a triagnle based on its side length
    side_a: int
    side_b: int
    side_c: int
    
    return type -> string
    """
    if not(side_a + side_b > side_c) or not(side_a + side_c > side_b) or not(side_b + side_c > side_a):
        return "invalid"
    elif side_a == side_b and side_b == side_c:
        return "equilateral"
    elif side_a == side_b or side_b == side_c or side_a == side_c:
        return "isosceles"
    else:
        return "scalene"

side_a, side_b, side_c = map(eval,input("Enter three sides of a triangle seperated by a space: ").split())
print(classify_triangle(side_a,side_b,side_c))

"""
sample:
input:      output:
3 4 5       scalene
5 5 5      equilateral
10 9 10    isosceles
1 10 1     invalid
"""