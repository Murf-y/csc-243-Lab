"""Write a Python program to sort a list of elements in a decreasing order using selection sort"""

def selectionSort(l):
    l_copy = l.copy()
    for i in range(len(l_copy)):
        min_index = i
        for j in range(i+1, len(l_copy)):
            if l_copy[j] > l_copy[min_index]:
                min_index = j
        if min_index != i:
            l_copy[i], l_copy[min_index] = l_copy[min_index], l_copy[i]
    return l_copy
def main():
    l = [1,241,3,1,51]
    l = selectionSort(l)
    print(l)
main()