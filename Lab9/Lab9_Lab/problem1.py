"""
Part A

create a function that take a string and create a file and put the string in it
"""

def create_file(filename, text):
    """
    create a file and put the string in it
    """
    with open(filename, 'w') as f:
        f.write(text)

"""
Part B
Create a program that reads a text file and create a text file with additional information such as:
•	Number of lines
•	Number of words
•	Number of characters
•	Number of occurrences of every alphabetic character in the file
"""

def read_file(filename):
    """
    read a file and return a string
    """
    with open(filename, 'r') as f:
        return f.read()
def modify_file(text):
    """
    create a file and put the string in it
    and add additional information
    """
    number_lines = len(text.split('\n'))
    number_words = len(text.split(' '))
    number_characters = len(text)
    number_occurrences = {}
    for char in text:
        if char.isalpha():
            if char in number_occurrences:
                number_occurrences[char] += 1
            else:
                number_occurrences[char] = 1
    with open('flanders_info.txt', 'w') as f:
        f.write(text)
        f.write('Number of lines: {}\n'.format(number_lines))
        f.write('Number of words: {}\n'.format(number_words))
        f.write('Number of characters: {}\n'.format(number_characters))
        f.write('Number of occurrences of every alphabetic character in the file: {}\n'.format(number_occurrences))


mystring = """
In Flanders Fields

In Flanders fields the poppies blow
Between the crosses, row on row,
That mark our place; and in the sky
The larks, still bravely singing, fly
Scarce heard amid the guns below.

We are the Dead. Short days ago
We lived, felt dawn, saw sunset glow,
Loved and were loved, and now we lie,
In Flanders fields.


Take up our quarrel with the foe:
To you from failing hands we throw
The torch; be yours to hold it high.
If ye break faith with us who die
We shall not sleep, though poppies grow

In Flanders fields.
"""

def main():
    
    create_file('flanders.txt', mystring)
    text = read_file('flanders.txt')
    modify_file(text)

if __name__ == '__main__':
    main()

"""
Sample run:
the sample run is in the files submitted with the lab (flanders.txt , flanders_info.txt)
"""
