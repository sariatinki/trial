import random

# message displyed just before begining the game
print("LET'S BEGIN THE GUESS GAME")

def numgenerator():
    return random.randrange(1,10)

num1 = numgenerator()
guess_count = 0

while True:
    userinput = input("ENTER A NUMBER BETWEEN 1-9:")

    if userinput == "exit":
        print("GAME OVER!!")
        break

    num = int(userinput)
    if num < num1:
        guess_count += 1
        print("GUESS TOO LOW")
    elif num > num1:
        guess_count += 1
        print("GUESS TOO HIGH")
    elif num == num1:
        guess_count += 1
        print("""WELLDONE!! YOU GOT IT RIGHT
              TOTAL GUESS:""", guess_count)
        num1 = numgenerator()
        guess_count = 0

   
    
