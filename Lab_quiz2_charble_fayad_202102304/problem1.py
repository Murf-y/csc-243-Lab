"""
write a function that takes a list and return a list with all the doctors in it
"""

def find_doctors(names):
    """
    takes a list of names and returns a list of doctors
    """
    return list(filter(lambda x: x.startswith('Dr.'), names))

