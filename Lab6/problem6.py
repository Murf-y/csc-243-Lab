"""
Problem6
A good way to learn a language and how it works is to implement some of its built-in functionality.
Do not use any of the List methods.

•	Write a function named total(a_list) that behaves exactly like the built-in function sum().
       >>> total( [1, 100, 3, 4, 5, 6] )
       119

•	Write a function named contains(a_list, item) that behaves exactly like the built-in operator item in a_list.
       >>> contains( ['alice', 20, True], 20 )
       True
       >>> contains( ['alice', 20, True], 'eugene' )
       False

•	Write a function named find(a_list, item) that behaves exactly like the built-in list method find().
       >>> find( ['alice', 20, True], True )
       2
       >>> find( ['alice', 20, True], 42 )
       -1

Write a driver program that tests the above 3 functions. That is would call each function at least two times.

"""
def total(a_list):
    """
    total( [1, 100, 3, 4, 5, 6] )
    119
    """
    total = 0
    index = 0
    while index < len(a_list):
        total += a_list[index]
        index += 1
    return total

def contains(a_list,item):
    """
    contains( ['alice', 20, True], 20 )
    True
    contains( ['alice', 20, True], 'eugene' )
    False
    """
    index = 0
    while index < len(a_list):
        if a_list[index] == item:
            return True
        index += 1
    return False

def find(a_list,item):
    """
    find( ['alice', 20, True], True )
    2
    find( ['alice', 20, True], 42 )
    -1
    """
    index = 0
    while index < len(a_list):
        if a_list[index] == item:
            return index
        index += 1
    return -1

a_list_1 = [1,2,3,4,5,6,7,8,9,10]
a_list_2 = [1,2,3,4,5]
total_1 = total(a_list_1)
total_2 = total(a_list_2)
print(f"{total_1=}  {total_2=}")

a_list_1 = ['alice', 20, True]
contains_1 = contains(a_list_1,20)
contains_2 = contains(a_list_1,'eugene')
print(f"{contains_1=}  {contains_2=}")

a_list_1 = ['alice', 20, True]
find_1 = find(a_list_1,True)
find_2 = find(a_list_1,42)
print(f"{find_1=}  {find_2=}")
