valid_input = ("rock", "paper", "scissors")
def player1():
    choice = input("PLAYER ONE:")
    if choice in valid_input:
        return choice
    else:
        choice = input("PLAYER ONE:")

def player2():
    choice = input("PLAYER TWO:")
    if choice in valid_input:
        return choice
    else:
        choice = input("PLAYER TWO:")

while True:
    p1 = player1()
    p2 = player2()
    if p1 == "rock" and p2 == "paper":
        print("PLAYER TWO WINS")
    if p1 == "rock" and p2 == "scissors":
        print("PLAYER ONE WINS")
    if p1 == "scissors" and p2 == "rock":
        print("PLAYER TWO WINS")
    if p1 == "scissors" and p2 == "paper":
        print("PLAYER ONE WINS")
    if p1 == "paper" and p2 == "rock":
        print("PLAYER ONE WINS")
    if p1 == "paper" and p2 == "scissors":
        print("PLAYER TWO WINS")
    if p1 == "rock" and p2 == "rock":
        print("DRAW")
    if p1 == "paper" and p2 == "paper":
        print("DRAW")
    if p1 == "scissros" and p2 == "scissors":
        print("DRAW")


    play1 = input("Do you wish to continue:")
    play2 = input("Do you wish to continue:")
    if play1 == play2 == "yes":
        continue
    else:
        print("GAME OVER")
        break

    
