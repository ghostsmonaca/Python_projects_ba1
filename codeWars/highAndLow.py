def high_and_low(numbers):
    return 0


def test():
    print(high_and_low("1 2 3 4 5"))  # return "5 1"
    print(high_and_low("1 2 -3 4 5"))  # return "5 -3"
    print(high_and_low("1 9 3 4 -5"))  # return "9 -5"


test()
