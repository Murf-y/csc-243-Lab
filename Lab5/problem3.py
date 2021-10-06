"""
Problem 3

Ask the user to enter his/her first name, Last name and ID number and then print 3 lines as follows: 

Input

Enter your first name, last name and ID (seperated by a space): Joe Khalife 12345

Output

Hi, my name is first name is Joe
My last name is Khalife
My ID is 12345
"""

first_name, last_name , ID = input("Enter your first name, last name and ID (seperated by a space): ").split()

print("Hi, my name is {}".format(first_name))
print("My last name is {}".format(last_name))
print("My ID is {}".format(ID))

"""
output:
Hi, my name is charbel
My last name is fayad
My ID is 202102394
"""