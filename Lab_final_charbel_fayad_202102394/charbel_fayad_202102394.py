# problem 1
def print_accordingly(list1,list2):
    for i in range(len(list1)):
        print(f"{list1[i]} wants a {list2[i]} for Christmas")

def problem1_main():
    nameList = ["Leo Nassar", "Joe Jabbour", "Windy Sander", "Cindy Woods"]
    giftsList = ["Ferrari", "Auto-corrector","Barbie", "doctor-kit"]
    print_accordingly(nameList,giftsList)

problem1_main()


# problem 2
class Submarine:
    def __init__(self,depth,descent_count):
        self.depth = depth
        self.descent_count = descent_count
    
    def getDepth(self):
        return self.depth
    def getDescentCount(self):
        return self.descent_count
    def setDepth(self,depth):
        self.depth = depth
    def setDescentCount(self,descent_count):
        self.descent_count = descent_count
    
    def descend(self,depth_change):
        if depth_change ==5 or self.descent_count + depth_change > 1000: return 
        self.descent_count += depth_change
    def ascend(self,depth_change):
        self.descent_count -= depth_change
    
# problem 3

def number_before_n(mylist,n):
    return [i for i in mylist if i >= n]


# Extra Problem 

def bubbleSort(mylist):
    for i in range(len(mylist)):

        for j in range(len(mylist)-1):
            if mylist[j] > mylist[j+1]:
                mylist[j+1] , mylist[j] = mylist[j], mylist[j+1]
    return mylist


