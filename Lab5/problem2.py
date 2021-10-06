"""
Write a program that reads a line of text and an integer and outputs the first and last word of the line each n times.

Hint: You may want to use the split method.
The split() method splits the string into a list of substrings 

Input

Enter a line of text:  Hi how are you all in the class
Enter an integer:  3

Output

HiHiHi      
classclassclass
"""

sentence = input("Enter a line of text: ")
n = int(input("Enter an integer: "))
print(sentence.split()[0] * n)
print(sentence.split()[-1] * n)

"""
output: 
Enter a line of text: charbel is cool
Enter an integer: 2
charbelcharbel
coolcool 
"""