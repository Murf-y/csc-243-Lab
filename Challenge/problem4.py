"""
Write a function that will take a string and returns the reverse of this string.
"""

def reverse_sentence(string):
    return string[::-1]

def main():
    sentence = input("Enter a sentence: ")
    reversed_sentence = reverse_sentence(sentence)
    print(reversed_sentence)
main()



"""SECRET WORD IS : waterman"""