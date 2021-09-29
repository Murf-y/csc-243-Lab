"""
Write a function that takes 2 integers x and y,
output should be their sum.However, sums in the range 10 till 19 inclusive,
are forbiddenm so in that case return 20.
Invoke the function 3 times to show the results.
"""
def special_sum(x, y):
    """
    x : int
    y: int
    return type -> int
    """
    if x + y in range(10, 20):
        return 20
    else:
        return x + y

print(special_sum(3,4))
print(special_sum(9,4))
print(special_sum(10,11))

"""
output:
7
20
21
"""