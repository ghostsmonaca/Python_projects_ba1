import random
f = open("Python_projects_ba1/week_5/words.txt", "rt")

with open("Python_projects_ba1/week_5/words.txt") as f:
   lines = f.readlines()
   amount = len(lines)

def choose_word():
    randomline = random.randint(0, amount)
    letters = len(lines[randomline])
    word = lines[randomline]
    game_start(letters, word)

def game_start(letters, word):
    lives = 10
    guessed = ""
    print("Welcome to hangman! Try to guess this random word. You get 10 lives.")
    print(" ")
    while lives != 0:
        wordGuess = letters * "_"
        print(f"You have {lives} lives left.")
        print(f"Guessed letters: {guessed}")
        print(f"{wordGuess}")
        guess = str(input("Please input ONE letter"))
        if guess in word:
            for x in range(0, letters):
                wordGuess[x].replace("_", guess)
                guessed += guess
                print(f"Good job!")
                print(f"{wordGuess}")
            print("Too bad!")
            
choose_word()
