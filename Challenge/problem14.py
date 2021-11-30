"""
Create a class called Student that has the following attributes:
- Name
- ID
- Major
- GPA
- Credits taken
1-Create a method in this class that will display the information of a student as follows:
2-Create a method that will take the grade of a class and the number of credits, add the number of
credits to the total credits taken by the students, and adjust the GPA based on the new grade.
How to calculate new gpa:
Ex: new grade=”A”, nbr_of_credits: 3, old_gpa=3.7, old_nbr_of_credits=30
“A” is 4 points so nbr_of_points=4
New_gpa= ((old_gpa* old_nbr_of_credits)+ nbr_of_credits*nbr_of_points)/(nbr_of_credits +
old_nbr_of_credits)
New_gpa=((3.7*30)+3*4)/33
New_gpa= 3.72
"""

class Student:
    def __init__(self, name, id, major, gpa, credits):
        self.name = name
        self.id = id
        self.major = major
        self.gpa = gpa
        self.credits = credits
    def display(self):
        print("Student ID: ", self.id)
        print("Student Name: ", self.name)
        print("Student Major: ", self.major)
        print("Student GPA: ", f"{self.gpa:.3f}")
    def add_grade(self, grade, credits):
        old_credits = self.credits
        self.credits += credits
        if grade == "A": 
            self.gpa = ((self.gpa * old_credits) + (4 * credits)) / (self.credits)
        elif grade == "B":
            self.gpa = ((self.gpa * old_credits) + (3 * credits)) / (self.credits)
        elif grade == "C":
            self.gpa = ((self.gpa * old_credits) + (2 * credits)) / (self.credits)
        elif grade == "D":
            self.gpa = ((self.gpa * old_credits) + (1 * credits)) / (self.credits)
        elif grade == "F":
            self.gpa = ((self.gpa * old_credits) + (0 * credits)) / (self.credits)


def main():
    murf = Student("Charbel Fayad", "202102394", "CS", 3.7, 30)
    murf.display()
    murf.add_grade("A", 3)
    murf.display()

main()