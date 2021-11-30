"""
Create a 2d array that contains a shape 
7 represents the borders of the shape, 1s are the content inside the shape,
and 0s are the outside of your shape.
The purpose of this game is to eliminate all 7s
Create a program that will keep asking the user to enter dimensions Ex : 1 5 (my2dlist[1][5])
Check the 2d list at these indeces. If, the number is 0 or 7 -> replace it by 2.
If the number is 1 print “you lost the game, bye!” and finish the program.
When all 7s are eliminated from the list, return “you win! To the next game!” and 
finish the program
"""

def create_shape():
    """
    Create a 2d array that contains a shape  of a diamond
    7 represents the borders of the shape, 1s are the content inside the shape,
    and 0s are the outside of your shape.
    """

    
    # row1   0s -> 11, 1s -> 0, 7s -> 0
    # row2   0s -> 10, 1s -> 0, 7s -> 1

    # row3   0s ->  8, 1s -> 1, 7s -> 2
    # row4   0s ->  6, 1s -> 3, 7s -> 2
    # row5   0s ->  4, 1s -> 5, 7s -> 2
    # row6   0s ->  2, 1s -> 7, 7s -> 2
    # row7   0s ->  4, 1s -> 5, 7s -> 2
    # row8   0s ->  6, 1s -> 3, 7s -> 2
    # row9   0s ->  8, 1s -> 1, 7s -> 2

    # row10  0s ->  10, 1s -> 0, 7s -> 1
    # row11  0s ->  11, 1s -> 0, 7s -> 0
    rows = 12
    shape = []
    sevens = 2
    ones = 1
    flip = False
    # diamond shape 
    for row in range(rows):
        if row == 0 or row == rows-1:
            shape.append([0] * 11)
        elif row == 1 or row == rows - 2:
            shape.append([0]*5+[7]+[0]*5)
        else:
            if ones == 7:
                flip = True
            if ones >= 1:
                zeros = 11 - sevens - ones
                shape.append([0]*(zeros//2)+[7]+[1]*ones+[7]+[0]*(zeros//2))
                
                if flip:
                    ones -=2
                    
                else:
                    ones +=2

    return shape

def validate_win(shape):
    "check number of sevens in the rows"
    for row in shape:
        if 7 in row:
            return False
    return True

def main():
    # i created the shape even tho we could have used it directly...
    shape = create_shape()
    while True:
        dimensions = list(map(int,input("Enter a row and column: ").split()))
        
        point= shape[dimensions[0]][dimensions[1]]
        if point == 0 or point == 7:
            shape[dimensions[0]][dimensions[1]] = 2
        elif point == 1:
            print("You lost the game, bye!")
            break
        if validate_win(shape):
            print("You won! To the next game!")
            break
main()