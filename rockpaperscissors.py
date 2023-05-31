import random

def gameWin(comp, you):
    if comp == you:
        print("Draw")
    elif comp == "Rock":
        if you == "Scissors":
            print("Comp wins")
        elif you == "Paper":
            print("You win")
    elif comp == "Paper":
        if you == "Rock":
            print("Comp wins")
        elif you == "Scissors":
            print("You win")
    elif comp == "Scissors":
        if you == "Paper":
            print("Comp wins")
        elif you == "Rock":
            print("You win")

you = input("Your Turn: Rock(1), Paper(2), Scissors(3): ")
if you == "1":
    you = "Rock"
elif you == "2":
    you = "Paper"
elif you == "3":
    you = "Scissors"
else:
    print("Invalid input. Please try again.")
    you = input("Your Turn: Rock(1), Paper(2), Scissors(3): ")
    if you == "1":
     you = "Rock"
    elif you == "2":
        you = "Paper"
    elif you == "3":
        you = "Scissors"


print(f"You chose {you}")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = "Rock"
elif randNo == 2:
    comp = "Paper"
elif randNo == 3:
    comp = "Scissors"

print(f"Computer chose {comp}")
gameWin(comp, you)
