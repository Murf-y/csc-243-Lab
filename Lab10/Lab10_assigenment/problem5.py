"""
Write a program that repeatedly prompts the user to enter a capital for a state.
Upon receiving the user input, the program reports whether the answer is correct. 
Assume that 50 states and their capitals are stored in a two-dimensional list, as shown below.
The program prompts the user to answer all the states’ capitals and displays the total correct count.
The user’s answer is not case sensitive. Implement the program using a list 
to represent the data in the following table.
"""


def process_states_file():
    file =  open('states_capital.txt', 'r')
    states_capital = []
    for line in file:
        line.strip()
        line = line.split()
        states_capital.append([line[0], line[-1]])

    return states_capital

def main():
    states_capital = process_states_file()
    correct_count = 0
    for state in states_capital:
        user_input = input('What is the capital of ' + state[0] + ': ')
        if user_input.lower() == state[1].lower():
            print('Your answer is correct!')
            correct_count += 1
        else:
            print(f"The correct answer should be {state[1]}")
    print('The correct count is ' + str(correct_count))

if __name__ == '__main__':
    main()
