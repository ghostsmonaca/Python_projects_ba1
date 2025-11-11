def find_it(seq):
    seq.sort()
    tocheck = seq[0]
    counter = 0
    for x in seq:
        if x == tocheck:
            counter += 1
        else:
            if counter % 2 == 0:
                tocheck = x
                counter = 1
                continue
            else:
                break
    return tocheck


def test():
    # print(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]))  # 10
    print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))  # 5


test()
