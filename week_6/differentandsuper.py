def set_difference(l1, l2):
    return {x for x in l1 if x not in l2} #als je itereert over l2 gaat die ieder element af, door te gaan over een set, kan het sneller gaan


def superlists(l1, l2):
    if len(l2) == 0:
        return True
    for x in l1:
        if x in l2:
            return True
    return False
 #return len(set(l1) - set(l2)) <= 0
 #return (set(1) & set(l2) == set(l2))

#ipv join functie -> lambda