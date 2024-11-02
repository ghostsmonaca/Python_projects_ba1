stuk = ("paard", "toren", "koningin", "loper")
speler = ("wit", "zwart")
letters = "abcdefgh"
numbers = "12345678"

def can_strike(board):
    return None

def toren(position):
    letter = position[0]
    number = position[1]
    toreturn = [x+number for x in letters if letter != x]
    return toreturn + [letter+y for y in numbers if number != y]

def paard(position):
    letter = position[0]
    number = position[1]
    boven = ""
    for x in range(0, len(letters)):
        if letters[x] == letter:
            boven += letters[x+1]
            boven += letters[x-1]
    


def test():
    print(toren("c6"))
    print(paard("c6"))
    print(can_strike([("paard", "zwart", "c6"), ("paard", "wit", "d4")]))

test()