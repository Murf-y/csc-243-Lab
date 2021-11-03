def readChoice(prompt):
    choice = input(prompt)
    while choice not in ["L", "R"]:
        choice = input(f"Please enter a valid choice, Try again: {prompt}")
    return choice

defected_tiles = ["L","L","R","L","R","R","R","R","L","R","L","L","L","R","L"]
chances = 10
round_number = 0
while round_number <= len(defected_tiles)-1:
    print(f"Iteration number {round_number}")
    choice = readChoice("Do you want to go left or right? L(for left) R(for right): ")
    if choice == defected_tiles[round_number]:
        print("You chose a defected tile, you lose a chance.")
        chances-=1
    else:
        print(f"You chose the right tile to step on")
    print(f"The number of chances you still have is {chances}")
    round_number +=1
    print("\n")
    if chances <= 0:
        break

if chances <= 0:
    print("You lost the game, 0 chances left!")
else:
    print("You reched your destination, Congrats!")
