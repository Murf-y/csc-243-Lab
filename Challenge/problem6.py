"""
Write a Python program to remove the characters which have odd index values of a given string.
"""

def remove_odd_index_characters(string):
    return string[::2]

def main():
    string = input("Enter a string: ")
    print(remove_odd_index_characters(string))

main()

"""THe secret word is: hungry"""
