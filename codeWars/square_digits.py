def square_digits(num):
    return ''.join([str(int(x)**2) for x in str(num)])

'''    num = str(num)
    tor = ""
    for x in num:
        tor += str(int(x)**2)
    return tor'''

def test():
    print(square_digits(9119))
test()
