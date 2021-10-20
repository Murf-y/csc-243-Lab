"""
Problem 1
Given three points of a triangle, you can compute the angles using the following formula:
Rewrite the above program by defining and calling the following two functions:
•	Distance: that takes four numbers representing two points and returns the distance between them.
•	Angle: that takes as arguments three sides of a triangle and returns an angle,

"""
import math

def distance(x1, y1, x2, y2):
    """
    Calculate the distance between two points
    x1: numeric
    x2: numeric
    y1: numeric
    y2: numeric

    return type -> numeric
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def angle(side_a,side_b,side_c):
    """
    Calculate the angle of a triangle using its three sides
    side_a: numeric
    side_b: numeric
    side_c: numeric

    return type -> numeric
    """
    return math.degrees(math.acos((side_a ** 2 - side_b ** 2 - side_c ** 2) / (- 2 * side_b * side_c)))

points = input("Enter three points: ").split(",")
x1,y1,x2,y2,x3,y3 = list(map(eval,points))
a = distance(x3, y3, x2, y2)
b = distance(x3, y3 ,x1, y1)
c = distance(x2, y2, x1, y1)

A = angle(a,b,c)
B = angle(b,a,c)
C = angle(c,b,a)

print("The three angles are: ", round(A,2), round(B,2), round(C,2))

"""
output for: 1, 1, 6.5,1,6.5,2.5

The three angles are:  15.26 90.0 74.74
"""