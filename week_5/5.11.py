def count_words(string):
    test = string.split()
    print(test)
    count = 0
    if string == "":
        return 0
    for char in string:
        if char == " " or char == "," or char.isdigit():
            count += 1
        elif string[0].isdigit():
            return 0
    
    return count+1 #+1 voor het laatste woord, aangezien er geen spaties meer zijn
