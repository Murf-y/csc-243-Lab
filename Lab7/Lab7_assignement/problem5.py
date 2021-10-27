"""
Problem 5

Write a Python program that helps students compute their one semester Grade Point Average (GPA).
Assume that the possible Letter Grades for courses are A, B, C, D or F.
"""


def readInt(prompt):
    """
    Reads an integer from the user and returns it.
    """
    num = input(prompt)
    while not num.isnumeric():
        num = input("Try again" + prompt)
    return int(num)
def readLetterGrade(prompt):
    """
    Reads a letter grade from the user and returns it.
    """
    grade = input(prompt)
    while grade not in "ABCDF":
        grade = input("Try again" + prompt)
    return grade

def gradePoint(letter_grade, credits_hours):
    """
    (str, int) => float
    Takes a letter grade and returns the corresponding GPA
    """
    if letter_grade == "A":
        return 4.0 * credits_hours
    elif letter_grade == "B":
        return 3.0 *  credits_hours
    elif letter_grade == "C":
        return 2.0 * credits_hours
    elif letter_grade == "D":
        return 1.0 * credits_hours
    elif letter_grade == "F":
        return 0.0 * credit_hours
number_of_courses = readInt("Enter number of courses you have: ")
total_credit_hours = 0
total_grade_points = 0


for i in range(1,number_of_courses+1):
    credit_hours = readInt(f"Enter credit hours for course {i}: ")
    letter_grade = readLetterGrade(f"Enter grade letter for course {i}: ")
    grade_point = gradePoint(letter_grade, credit_hours)
    total_grade_points += grade_point
    total_credit_hours += credit_hours
GPA= total_grade_points / total_credit_hours
print(f"Your GPA is {GPA:.2F}")
