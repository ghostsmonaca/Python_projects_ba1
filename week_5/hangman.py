import random
f = open("Python_projects_ba1/week_5/words.txt", "rt")

with open("Python_projects_ba1/week_5/words.txt") as f:
   lines = f.readlines()
   amount = len(lines)

def choose_word():
    randomline = random.randint(0, amount)
    word = lines[randomline]
    word = word.lower()
    word = word.strip()
    game_start(word)

def game_start(word):
    lives = 10
    guessed = ""
    letters = len(word)
    print("Welcome to hangman! Try to guess this random word. You get 10 lives.")
    print(" ")
    wordGuess = ' '.join(letters * "_")
    wordGuess = wordGuess.split()
    
    while lives != 0:
        if ''.join(wordGuess) == word:
            winner(wordGuess, word)
            break
        else:
            print(f"{''.join(wordGuess)}")
            guess = str(input("Please input ONE letter"))
            print(" ")
            if guess in word:
                for char in range(0, len(word)):
                    if word[char] == guess:
                        wordGuess[char] = guess
                guessed += guess
                print("Good job!")
                print(" ")
                        
            else:
                print("Too bad!")
                guessed += guess
                lives -= 1
                
            print(f"You have {lives} lives left.")
            print(f"Guessed letters: {guessed}")
            print(" ")
    fail(lives, word)
    
def fail(lives, word):
    if lives == 0:
        print(f"You failed! The word was: {word}")
def winner(wordGuess, word):
    wordGuess = ''.join(wordGuess)
    if wordGuess == word:
        print(F"Congratulations! The word was: {word}")

choose_word()
