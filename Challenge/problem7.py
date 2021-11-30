"""Show 2 ways of finding the length of a list"""

def first_way(list1):
    return len(list1)

def second_way(list1):
    count = 0
    for _ in list1:
        count +=1
    return count
def main():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(first_way(list1))
    print(second_way(list1))
main()