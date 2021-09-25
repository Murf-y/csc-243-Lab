"""
Problem 6
Write a program that reads the (x,y) coordinates for two points (x1, y1) and (x2, y2). 
Compute the distance between the two points using the following formula:
Distance 
"formula" 
Input
2 3  and 6 5
Output
d = 4.47214
"""

import math

# read the coordinates of the two points
x1, y1 = input("Enter the coordinates x1 and y1 seperated by space: ").split(" ")
x2, y2 = input("Enter the coordinates x1 and y1 seperated by space: ").split(" ")

# calculate the distance using the following formula :
d = math.sqrt((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2)

# output the reuslt to the user
print("The distance between the two points is: ", round(d, 5))

