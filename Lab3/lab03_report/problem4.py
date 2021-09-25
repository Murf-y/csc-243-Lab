"""
Problem 4
Write a program that reads a 2-word String separated with a space. Duplicate each word alone and then concatenate them print two strings: 
The first printed String must be separated with a space in-between and the second printed String all stuck together. Remember you can always use the ‘+’ sign to concatenate Strings.

Input

Enter a 2-word String:  Hi class

Output

HiHi classclass        (here the 2 strings are separated by a space)
HiHiclassclass         (here it’s not!)
"""

# first methode using slice operator and find method
sentence = input("Enter a 2 words seperated by a space: ")
space_index = sentence.find(" ")
first_word = sentence[:space_index]
last_word = sentence[space_index + 1:]
print(first_word * 2 , last_word * 2)
print(first_word * 2+ last_word * 2, sep="")

# second methode using splitfy j
sentence = input("Enter a 2 words seperated by a space: ")
words = sentence.split(" ")
print(words[0] * 2, words[1] * 2)
print(words[0] * 2 + words[1] * 2, sep="")
