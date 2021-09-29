"""
Write a function that takes a string and return True if the string "cat" and "dog" 
appear the same number of times in the given string.Invoke the function 3 times to show your results.
"""

def cat_dog(sentence):
    return sentence.count("cat")==sentence.count("dog")

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))

"""
output
True
Flase
True
"""