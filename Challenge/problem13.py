"""
Write a Python program to search through a list sorted in a 
decreasing order using binary search."""

def binary_search(l, x):
    # l is sorted in a decreasing order
    low = len(l) - 1
    high = 0
    while low >= high:
        mid = (low + high) // 2
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            low = mid - 1
        else:
            high = mid + 1
    return -1



def main():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l.sort(reverse=True)
    print(binary_search(l, 5))

main()