"""
Problem 2
Write a program that read positive numbers until 0 is entered and output count, sum and average of the numbers entered:

"""

sum = 0
count = 0
def readPosInt():
    num = input("Enter a positive number, or 0 to stop: ")
    if num.isnumeric() and int(num) >=0:
        return int(num)
    else:
        return readPosInt()
num = readPosInt()

while num != 0:
    sum += num
    count += 1
    num = readPosInt()
print("The number of numbers entered is:", count)
print("The sum of the numbers entered is:", sum)
print("The average of the numbers entered is:", sum/count if count > 0 else 0)