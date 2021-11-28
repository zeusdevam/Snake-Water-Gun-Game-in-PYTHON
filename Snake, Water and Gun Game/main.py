import random


def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you== 'w':
            return False
    elif you=='g': 
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you== 's':
            return True    
    elif comp == 'g':
        if you == 's':
            return False
        elif you== 'w':
            return True       

print("Comp turn: snake(s) water(g) or gun(g)?")
randNO = random.randint(1, 2)
print(randNO)
if randNO == 1:
    comp = 's'
if randNO == 2:
    comp = 'w'    
if randNO == 3:
    comp = 'g'  

you = input("Your turn: snake(1) water(2) or gun(3)?")

a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")


if a == None:
    print("The game is a tie!")
elif a:
    print("You win")
else:
    print("You lose!")    