"""Problem 1:
Implement a variation of the Selection and of the Insertion sort function in such a way to display the list before being sorted and to display the content of the list at each iteration. 
Write a program that:
•	Reads from Keyboard numbers and stores them in a List1 
•	Makes a copy of List1 and call List2. 
•	Calls Selection sort on List1 and Calls insertion Sort on List2
"""
def readInt(prompt):
    num = input(prompt)
    while not num.isnumeric():
        num = input("Try again "+ prompt)
    return int(num)
def readListFromUser():
    """
    Reads from Keyboard numbers and stores them in a List1
    """
    numbers = input("Enter numbers separated by space: ").split()
    return list(map(int, numbers))

def displayList(list):
    """
    Displays the list
    """
    print("List: ", end="")
    for i in list:
        print(i, end=" ")
    print()

def insertionSort(list):
    """
    Sorts the list using insertion sort
    """
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
            j -= 1
        displayList(list)

def selectionSort(list):
    """
    Sorts the list using selection sort
    """
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j
        if min != i:
            list[i], list[min] = list[min], list[i]
        displayList(list)
def main():
    list1 = readListFromUser()
    list2 = list1.copy()
    print("List before sorting using selection sort: ")
    displayList(list1)
    selectionSort(list1)
    print("List before sorting using insertion sort: ")
    displayList(list2)
    insertionSort(list2)

if __name__ == "__main__":
    main()
