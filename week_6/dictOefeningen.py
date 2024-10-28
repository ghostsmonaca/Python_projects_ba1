def merge_dictionaries(d1, d2):
    d1.update(d2)
    return d1

def multiply_keys(d):
    total = 1
    for x in d:
        total *= d[x]
    return total

def reverse_lookup(d, v):
    return [x for x in d if d[x]==v]

def count_duplicates(s):
    s = s.split()
    d = {}
    for x in s:
        if x not in d:
            if s.count(x) <= 1:
                continue
            else:
                d[x] = s.count(x) 
    keys = list(d.keys())
    keys.sort()
    return [(x, d[x]) for x in keys]

def character_counts(s):
    s = s.lower()
    s = [x for x in s]
    s.sort()
    tr = list(set([(x, s.count(x)) for x in s if x != ' ']))
    tr.sort()
    return tr

