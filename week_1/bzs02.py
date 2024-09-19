import math

print("Hello", "World")
print("Hello", "World", sep="---")

#Onderste worden aan elkaar geplakt
print("Hello", end=" ")
print("World")

natlogaritme = int(input("Geef een getal"))
print(math.log(natlogaritme))
print(f'{math.log(natlogaritme):.3f}')

#gebruik van f strings belangrijk
print(f'Logaritme: {math.log(natlogaritme):.3f}')

#----------------- Hoorcollege
#\n -> code voor een enter

a = int(input("Geef getal 1: "))
b = int(input("Geef getal 2: "))
c = int(input("Geef getal 3: "))

reeks = [a, b, c]
reeks.sort()

for x in reeks:
    print(x, sep="<")
