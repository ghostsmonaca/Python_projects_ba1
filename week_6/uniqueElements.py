def unique_words(s):
    s = s.lower()
    s = s.split()
    s = list(set(x for x in s))
    s.sort()
    return s

def test():
    print(unique_words("This is a sample text with several words This is more sample text with some different words"))
#test()

def unique_letters(s1, s2):
    r1 = [x for x in s1 if x in s2]
    r2 = [x for x in s1 if x not in s2]
    r3 = [x for x in s2 if x not in s1]
    l = [list(set(r1)), list(set(r2)), list(set(r3))]
    for x in l:
        x.sort()
    return [''.join(x) for x in l]
