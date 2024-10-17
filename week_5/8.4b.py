line = "letters in het alfabet"
line = line.lower()
line = line.replace(" ", "")

alfalijst= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#a = 97
for char in line:
    place = ord(char)
    place = place - 97
    alfalijst[place] += 1
print(alfalijst)