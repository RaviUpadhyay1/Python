import random
# Snake Water Gun
def gameWin(comp, you):
    if comp == you:
        return None
    #check for all possiblities when computer chose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
        #check for all possiblities when computer chose w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
        #check for all possiblities when computer chose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
# print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = "w"
elif randNo == 3:
    comp = "g"

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)
# print("Computer chose ",comp)
# print("You chose ",you)
print(f"Computer chose {comp}")
print(f"You chose {you}")

if  a == None:
    print("The game is tie!")
elif a:
    print("You win!")
else:
    print("You lose!")
