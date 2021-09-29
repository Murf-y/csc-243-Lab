"""
Problem 4 

Design and write a Python program that will from Keyboard read four inputs, named test1, test2, test3, and final. The application will then determine the best 2 (Btest1, and Btest2) out of the 3 grades of tests 1, 2 and 3. Then, it will compute the final average and the letter grade. 

Use the following grading policy:
BTest1: 30%    BTest2: 30%       Final:  40%

And then display the corresponding letter-grade based on the following scheme:
90-100: A     80-89: B       70-79: C        60-69: D        59 and below: F
"""

def get_best_tests(test1, test2, test3):
    """
    return the 2 best between three tests
    test1: int
    test2: int
    test3: int
    return type -> int, int
    """
    tests_list = [test1,test2,test3]
    tests_list.sort()
    return tests_list[-1], tests_list[-2]
def compute_average(test1,test2,test3,final):
    """
    compute the best 2 test between test 1,2 and 3
    then return the average followin the grading policies
    test1: int
    test2: int
    test3: int
    final: int
    
    return type -> float
    """
    Btest1 , Btest2 = get_best_tests(test1,test2,test3)
    average = 0.3 * Btest1 + 0.3 * Btest2 + 0.4 * final
    return average
def compute_letter_grade(average):
    """
    compute the letter grade based on the average
    average: float
    
    return type -> str
    """
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

print("Grade Computing Application")
print("By Charbel.F")
print("---------------------------\n")

test1 = eval(input("Enter Test1:\n"))
test2 = eval(input("Enter Test2:\n"))
test3 = eval(input("Enter Test3:\n"))
final = eval(input("Enter Final:\n"))

computed_average = compute_average(test1, test2, test3, final)
print("\nComputed Average: ", computed_average)

computed_letter_grade = compute_letter_grade(computed_average)
print("Computed Letter Grade: ", computed_letter_grade)
print("\nThank you.")


"""
sample:
Grade Computing Application
By Charbel.F
---------------------------

Enter Test1:
10
Enter Test2:
100
Enter Test3:
70
Enter Final:
100

Computed Average:  91.0
Computed Letter Grade:  A

Thank you.
"""