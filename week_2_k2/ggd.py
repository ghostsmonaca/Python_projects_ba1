def ggd(a, b):
    if a % b == 0 or b % a == 0:
        return a
    else:
        return ggd(a -1, b)

def max(a, b):
    if a < b:
        return ggd(a, b)
    else:
        return ggd(b, a)


def test():
    print(max(14 , 21))
    print(max(12, 24))

test()