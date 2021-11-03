import random
import time

# Define the constants
Categories = ["Addition", "Substraction", "Multiplication"]
points = {}
time_allocated = {}
Num_of_questions_for_each_category = 10
difficulities = [1,2,3,4,5,6,7,8,9,10]
questions = {}

def generate_randInt_based_on_diffuclity_and_category(difficulity, category, categories):
    """
    Generate a random integer based on the difficulity and category
    (int) -> int
    """
    buffer = 1 if category == categories[2] else 10
    lower_seed = buffer * (difficulities[difficulity]-1)
    lower_range = lower_seed - 20 if lower_seed >= 20 else lower_seed
    upper_range = buffer * difficulities[difficulity]
    return random.randint(lower_range, upper_range)

def swap_to_get_biggest_number(num1, num2):
    """
    Swap the numbers to get the biggest number
    (int, int) -> int
    """
    if num1 > num2:
        return num1,num2
    else:
        return num2, num1

def get_two_num_based_on_difficulity_and_category(difficulity, category , categories):
    """
    Get two random numbers based on the difficulity
    (int) -> int, int
    """
    num1 = generate_randInt_based_on_diffuclity_and_category(difficulity,category, categories)
    num2 = generate_randInt_based_on_diffuclity_and_category(difficulity, category, categories)
    return swap_to_get_biggest_number(num1, num2)

def insert_question_with_answer(category, difficulity, categories):
    """
    Insert a question and its answer based on the category and difficulity to the questions dictionary
    (str, int) -> str
    """
    question = ""
    if category == "Addition":
        a,b = get_two_num_based_on_difficulity_and_category(difficulity,category, categories)
        question = str(a) + " + " + str(b)
        answer = eval(question)
        question +=  " = "
        questions[categories[0]][question] = answer
    
    elif category == "Substraction":
        a,b = get_two_num_based_on_difficulity_and_category(difficulity, category,categories)
        question = str(a) + " - " + str(b)
        answer = eval(question)
        question +=  " = "
        questions[categories[1]][question] = answer
    elif category == "Multiplication":
        a,b = get_two_num_based_on_difficulity_and_category(difficulity, category , categories)
        question = str(a) + " * " + str(b)
        answer = eval(question)
        question +=  " = "
        questions[categories[2]][question] = answer

def generate_questions_and_answers(number_of_questions, categories):
    """
    Generate questions and answers based on the number of questions
    (int) -> None
    """
    for category in categories:
        difficulity = 0
        for _ in range(number_of_questions):
            insert_question_with_answer(category, difficulity, categories)
            difficulity += 1

def initialize_questions_dict(categories):
    """
    Initialize the questions dictionary
    """
    for category in categories:
        questions[category] = {}
def initialize_time_dict(categories):
    """
    Initialize the questions dictionary
    """
    for category in categories:
        time_allocated[category] = 0

def initialize_points_dict(categories):
    """
    Initialize the questions dictionary
    """
    for category in categories:
        points[category] = 0


def readInt(message):
    """
    Read an integer from the user
    (str) -> int
    """
    num = input(message)
    while not num.isnumeric():
        num = input(f"Please enter an integer only, Try again: {message}")
    return int(num)

def validate_answer(user_answer, question, start_time, end_time, category):
    """
    Validate the answer and update the points and time_allocated
    (int, int, float, float, str) -> None
    """
    category_question  = questions[category]
    actual_answer = category_question[question]
    difficulity = difficulities[[i for i,e in enumerate(category_question.keys()) if e==question][0]]
    time_limit = 10 if difficulity in range(1,5 + 1) else 15
    time_took = end_time - start_time
    time_allocated[category] = time_allocated[category] + time_took
    print("\n")
    if user_answer == actual_answer:
        print("Correct!")
        print(f"You took {time_took:.1F} seconds to answer")
        if time_took <= time_limit:
            points[category] += 1
            print(f"You earned a point for {category}")
        else:
            points[category] -= 1
            print(f"You lost a point for {category}")
    else:
        print("Wrong!")
        print(f"The correct answer is {actual_answer}")
        points[category] -= 1
        print(f"You lose a point in {category}")
    print("_________________________________________\n")
    

def ask_questions(categories):
    """
    Ask the questions from the questions dictionary for each category
    (str) -> None
    """
    for category in categories:
        print("\n" + category + ":\n")
        for question in questions[category]:
            start_time = time.time()
            answer = readInt(f"{question}")
            end_time = time.time()
            validate_answer(answer, question, start_time, end_time, category)
            time.sleep(2)

def print_result(categories):
    """
    Print the result
    """
    print("\n\n")
    print("Your result:")
    categories_line = "Categories: "
    categories_line += " | ".join([f"{i:8}" for i in categories])
    points_line = "Points: "
    points_line += "".join([f"{i:8}" for i in points.values()])
    time_line = "Average Time: "
    time_line += "".join([f"{round(i/Num_of_questions_for_each_category, 2):8}" for i in time_allocated.values()])
    
    print(categories_line)
    print(points_line)
    print(time_line)

    average_points = (sum(points.values()) // Num_of_questions_for_each_category*len(categories))*100
    average_time = sum([i for i in time_allocated.values()])//len(time_allocated.values())
    print(f"Average Points is {average_points:.2F}")
    print(f"Average Time is {average_time:.2F} seconds per question")
    if average_points >= 50:
        print("Congrats, You passed the test!")
    else:
        print("Sorry, you did not pass, consider taking the test again")
    print("\n")

def main():
    initialize_questions_dict(Categories)  
    initialize_time_dict(Categories)   
    initialize_points_dict(Categories)
    generate_questions_and_answers(Num_of_questions_for_each_category, Categories)
    print("\n\n")
    print("Welcome to mathSurf!")
    print("__________________")
    print("You have 10 to 15 seconds to answer each question depending to its difficulity")
    print("If you fail to answer in the given time you lose a point")
    print("If you answer correctly you earn a point")
    print("Good Luck!")
    time.sleep(5)
    ask_questions(Categories)
    print_result(Categories)


if __name__ == "__main__":
    main()