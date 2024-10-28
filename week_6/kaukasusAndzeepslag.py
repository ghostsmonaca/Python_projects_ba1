def voorkomens(s):
    s = s.lower()
    s = [x for x in s]
    tr = {x: s.count(x) for x in s if x != ' '}
    keys = list(tr.keys())
    keys.sort() #sort hoefde niet
    return {x: tr[x] for x in keys}

def evenwichtig(d):
    di = voorkomens(d)
    valuelist = list(di.values())
    for x in valuelist:
        if x != valuelist[0] or x == 1:
            return False
    return True

#print(evenwichtig("aaabbccccddd"))

#empty list


def boot_overlappend(boot1, rooster):
    for x in boot1:
        if x in rooster:
            return True
    return False
#kan met disjoint en met & 
def boot_toevoegen(boot1, rooster):
    if boot_overlappend(boot1, rooster) == True:
        return rooster
    return rooster | boot1

def vuur(vakje, rooster):
    if vakje in rooster:
        rooster.remove(vakje)
        return (True, rooster)
    return (False, rooster)
