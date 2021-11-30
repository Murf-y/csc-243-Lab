"""Write a Python function to check whether a number is perfect or not"""

def is_perfect(num):
    if num == 0:
        return False
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False

def readInt(prompt):
    num = input(prompt)
    while not num.isnumeric():
        print("Please enter a valid positive number.")
        num = input(prompt)
    return int(num)
def main():
    num = readInt("Enter a number: ")
    if is_perfect(num):
        print(f"The number {num} is perfect.")
    else:
        print(f"The number {num} is not perfect.")

main()