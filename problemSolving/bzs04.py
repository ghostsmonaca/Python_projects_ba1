def open_lockers(num_lockers):
    lockers = [0] * (num_lockers + 1)
    
    for person in range(1, num_lockers + 1):
        # De persoon draait elk kastje om dat een veelvoud is van hun nummer: 
        for locker in range(person, num_lockers + 1, person): #De laatste 'Person' geeft aan welk veelvoud ze moeten omdraaien
            lockers[locker] = 1 - lockers[locker]  # Wissel 0 naar 1 of 1 naar 0
        print(f"{person}: {lockers[1:]}")
    
    open_lockers = [i for i in range(1, num_lockers + 1) if lockers[i] == 1]
    return open_lockers


num_lockers = 30
result = open_lockers(num_lockers)
print(f"Open: {result}")
