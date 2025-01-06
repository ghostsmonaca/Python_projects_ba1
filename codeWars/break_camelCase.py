def solution(s):
    tor = ""
    for x in s:
        if x.isupper():
            tor += " "
            tor += x
        else:
            tor+=x
    return tor

def test():
    print(solution("breakCamelCase"))

test()