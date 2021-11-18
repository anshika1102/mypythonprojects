import random


def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp == 's':
        if you == 's':
            return True
        elif you == 'r':
            return False


while 1:
    print("LET'S BEGIN")
    print("Comp Turn :Rock(r) Paper(p) or Scissors(s)?")
    randNo = random.randint(1, 3)
    if randNo == 1:
        comp = 's'
    elif randNo == 2:
        comp = 'r'
    elif randNo == 3:
        comp = 'p'

    you = input("Your Turn : Rock(r) Paper(p) or Scissors(s)? ")
    a = gameWin(comp, you)

    print(f"Computer Chose {comp}")
    print(f"You Chose {you}")

    if a == None:
        print("The game is a tie!")
    elif a:
        print("You Win!")
    else:
        print("You Lose!")
