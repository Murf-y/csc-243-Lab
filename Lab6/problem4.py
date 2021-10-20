"""
Problem 4
Write a function that checks whether two words are anagrams.
Two words are anagrams if they contain the same letters. For example, silent
and listen are anagrams. The header of the function is:

def isAnagram(s1, s2):

(Hint: Obtain two lists for the two strings. Sort the lists and check if two lists
are identical.)

Write a test program that prompts the user to enter two strings and, if they
are anagrams, displays YES (All Capital) if is an anagram; otherwise, it displays NO (All Capital) if is not an anagram.

"""
def isAnagram(s1, s2):
    """
    This function checks if two words are anagrams.
    Two words are anagrams if they contain the same letters.
    For example, silent and listen are anagrams.
    """
    # Convert the strings to lists
    s1 = list(s1)
    s2 = list(s2)

    # Sort the lists
    s1.sort()
    s2.sort()

    # Check if the two lists are identical
    if s1 == s2:
        return True
    else:
        return False
sentence_one = input("Enter a word: ")
sentence_two = input("Enter another word: ")
if isAnagram(sentence_one, sentence_two):
    print("YES")
else:
    print("NO")
