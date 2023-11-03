def commaCode(myList):
    string = ""
    if myList == "":
        return ""
    
    toList = myList.split()
    for i in range(len(toList)-1):
        string += toList[i] + ", "
    if len(toList) > 1:
        string += "and " 
    string += toList[len(toList)-1]
    return(string)

myList = input("Input: ")
print(commaCode(myList))

# split
# join by index
# sep with comma
# last: and 

text = 3.444
print(f'---{text:^5.2f}-')