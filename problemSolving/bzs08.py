def db():
    total = 100/100
    typeA = 99/100
    typeB = 1/100

    total = typeA + typeB
    typeA = typeA - (1/100)
    total = typeB + typeA
    print(typeA/100)

db()