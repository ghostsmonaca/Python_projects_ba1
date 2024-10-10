import random

def start():
    print("Welcome! Choose a number of rounds and a number of digits to guess")
    rounds = int(input("How many rounds would you like to guess?"))
    digits = int(input("How many digits do you wish the numeric code to include?"))
    print("Good luck!")
    numericCode(rounds, digits)

def numericCode(rounds, digits):
    code = []
    for x in range(digits):
        randomnum = int(random.randint(0,9))
        randomnum = str(randomnum)
        code.append(randomnum)
    game(rounds, digits, code)

def game(rounds, digits, code):
    guess = []
    counter = 0
    while counter != rounds:
        guess = list(input(f"Please enter {digits} digits to try"))
        greturn = []
        while len(guess) != len(code):
            guess = list(input(f"Please {digits} at the same time and press enter"))
        if guess != code:
            for x in range(0, digits):
                if code[x] == guess[x]:
                    greturn.append(guess[x])
                elif guess[x] in code:
                    greturn.append("X")
                elif guess[x] not in code:
                    greturn.append(".")
        else:
            print("Congratulations! You won!")
            print(f"The code was: {code}")
            break
        counter += 1
        print(greturn)

    if counter == rounds:
        print("You fail!")
        print(f"The code was: {code}")
start()
