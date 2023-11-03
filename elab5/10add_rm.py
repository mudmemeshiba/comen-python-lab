numList = list(map(int,input().split()))
menu,x = input().split()
while menu != "E":
    x = int(x)
    if menu == "A":
        numList.append(x)
    elif menu == "S":
        print(numList[x])
    elif menu == "R":
        numList.remove(numList[x])
    elif menu == "E":
        break
    # loop
    menu,x = input().split()    
print(*numList)