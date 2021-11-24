"""
Implement a class named Rectangle to represent a rectangle. The class contains:
•	Two data fields named width and height.
•	A constructor that creates a rectangle with the specified width and height. The default values are 1 and 2 for the width and height, respectively.
•	A method named getArea() that returns the area of this rectangle.
•	A method named getPerimeter() that returns the perimeter.

Write a test program that creates two Rectangle objects—one with width 4 and height 40 and 
the other with width 3.5 and height 35.7. (you can read them from the user or just put them 
directly in your code) Display the width, height, area, and perimeter of each rectangle in 
this order (in the main. Just create 2 rectangles instances and call the 4 functions on each 
of the rectangles. And print their results)
"""


class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * self.width + 2 * self.height

def main():
    rect1 = Rectangle(4, 40)
    rect2 = Rectangle(3.5, 35.7)
    print("Rectangle 1:")
    print("Width:", rect1.getWidth())
    print("Height:", rect1.getHeight())
    print("Area:", rect1.getArea())
    print("Perimeter:", rect1.getPerimeter())
    print()
    print("Rectangle 2:")
    print("Width:", rect2.getWidth())
    print("Height:", rect2.getHeight())
    print("Area:", rect2.getArea())
    print("Perimeter:", rect2.getPerimeter())

main()