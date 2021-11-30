"""
Write a Python program to sort a list of elements using the bubble sort algorithm."""

def bubbleSort(l):
    l_copy = l.copy()
    for i in range(len(l_copy)):
        for j in range(i+1, len(l_copy)):
            if l_copy[i] > l_copy[j]:
                l_copy[i], l_copy[j] = l_copy[j], l_copy[i]
    return l_copy
def main():
    l = [1, 5, 3, 2, 4]
    l = bubbleSort(l)
    print(l)
main()
