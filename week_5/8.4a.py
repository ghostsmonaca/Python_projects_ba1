namelist = []
name = str(input("Input a name")) 
namelist.append(name)
while name != "":
    name = str(input("Input a name"))  
    namelist.append(name)
namelist.sort()
namelist.pop(0)
print(namelist)