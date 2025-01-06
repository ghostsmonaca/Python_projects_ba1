def high(s):
    s = s.split()
    points = [c+c for c in[(ord(x)-96) for x in s]][-1]
    
def test():
    print(high("abad gg kkd"))

test()