def sumSubList(numList, x, y):
    subList = numList[x:y+1]
    sumSubList = sum(subList)
    return sumSubList

def printsumSubList(numList, x, y):
    while True:
        if not (-1*len(numList) <= x <= len(numList)-1) and (-1*len(numList) <= y <= len(numList)-1):
            print("x Bad Input")
        elif not (-1*len(numList) <= y <= len(numList)-1) and (-1*len(numList) <= x <= len(numList)-1):
            print("y Bad Input")
        elif not (-1*len(numList) <= y <= len(numList)-1) and not (-1*len(numList) <= x <= len(numList)-1):
            print("x and y Bad Input")

        if (-1*len(numList) <= x <= len(numList)-1) and (-1*len(numList) <= y <= len(numList)-1):
            xpos = x % len(numList)
            ypos = y % len(numList)
            if xpos > ypos:
                break

        # check if x is on the right of y
        if -1*len(numList) <= x <= len(numList)-1 and -1*len(numList) <= y <= len(numList)-1:
            #  to positive index
            if x < 0:
                x = x % len(numList)
            if y < 0:
                y = y % len(numList)
            #if x is on the right of y (pos x > y)
            if x > y:
                break
            print(sumSubList(numList, x, y))

        index   = input("")
        x,y     = [int(i) for i in index.split()]
    print()

num     = input("")
numList = [int(i) for i in num.split()]
index   = input("")
x,y     = [int(i) for i in index.split()]
printsumSubList(numList, x, y)
