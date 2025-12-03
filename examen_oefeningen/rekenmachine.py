def evaluate(bewerking):
    bewerking = removeSpaces(bewerking) + "#"
    eerste_char = True
    resul = ""
    teken = ""
    tweede_nummer = ""
    for character in bewerking:
        if character in "0123456789." and teken != "":
            eerste_char = False
            tweede_nummer += character
            teken = ""
            tweede_nummer = ""

        elif character in "+/*-^#":
            teken += character
            if eerste_char == False and tweede_nummer != "":
                if teken == "+":
                    resul = plus(resul, tweede_nummer)
                elif teken == "-":
                    resul = min(resul, tweede_nummer)
                elif teken == "*":
                    resul = maal(resul, tweede_nummer)
                elif teken == "/":
                    resul = deel(resul, tweede_nummer)
                elif teken == "^":
                    resul = macht(resul, tweede_nummer)
        elif eerste_char:
            resul += character
    return resul


def removeSpaces(bewerking):
    return "".join([x for x in bewerking if x != " "])


def plus(x, y):
    return float(x) + float(y)


def min(x, y):
    return float(x) - float(y)


def maal(x, y):
    return float(x) * float(y)


def deel(x, y):
    if float(y) == 0:
        return "NaN"
    return float(x) / float(y)


def macht(x, y):
    if "." in y:
        return "NaN"
    return float(x) ** float(y)


def test():
    print(evaluate("3 + 5"))
    # print(evaluate("10 - 2* 3"))
    print(evaluate("3^2 + 1"))
    # print(evaluate("5.5 + 2*3 -1"))
    print(evaluate("5 + 16"))


test()
