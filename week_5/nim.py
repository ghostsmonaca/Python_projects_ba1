n = int(input("How many rows would you like to play with?"))
player = 1
rowslist = []
total = 0
for x in range(1,n+1):
    print("0"*x)
    total += 1*x
    rowslist.append("0"*x)

kopie = rowslist[:]
print(rowslist)
lengte = len(kopie)

def printlist(kopie):
    for x in range(0, len(kopie)):
        print(kopie[x])
    
def whichplayer():
    if player % 2 != 0:
        return "Player 1"
    return "Player 2"
#yasmines idea, genius


while total != 1:
    playernow = whichplayer()   
    print(total)
    print(playernow)
    row = int(input("Which row would you like to take away from?"))-1
    amount = int(input("How many beads do you wish to take away?"))
    
    amountleft = len(kopie[row]) - (amount)
    total -= amount
    if amountleft <= 0:
        kopie[row] = ""
    else:
        kopie[row] = amountleft * "0"
    printlist(kopie)
    player += 1

print(f"{playernow} has lost")
