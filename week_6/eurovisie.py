def scoresToevoegen(dCountries, dAddpoints):
    for x in dCountries:
        total = dAddpoints[x]
        dCountries[x] += total
    
def scoresTonen(dCountries, amount = 0):
    toget = amount
    if amount == 0:
        toget = len(dCountries.keys())
    valuesD = list(dCountries.values())
    valuesD.sort()
    sorted_dict = {}
    for key in sorted(dCountries, key=dCountries.get, reverse=True):
        sorted_dict[key] = dCountries[key]
    returnlist = []
    for x in range(toget):
        for x in sorted_dict:
            returnlist.append((x, sorted_dict[x]))
    return returnlist


scorebord = {}
scores_UK = {'Lithuania': 7, 'Russia': 3, 'Estonia': 4, 'Azerbaijan': 2, 'Sweden': 12, 'Turkey': 1, 'Spain': 8, 'Germany': 6, 'Malta': 5, 'Ireland': 10}
scoresToevoegen(scorebord, scores_UK)
print(scoresTonen(scorebord))

#gebruik van lambda functies is heel bela,grijk