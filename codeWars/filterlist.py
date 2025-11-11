def filter_list(l):
    returnList = []
    for f in l:
        if type(f) == int:
            returnList.append(f)
    return returnList


# return [x for x in l if type(x) is not str]


def test():
    print("testcase: ", filter_list([1, 2, "a", "b", "3"]))


test()
