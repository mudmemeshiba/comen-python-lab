x = int(input())
y = int(input())
p = int(input())
count = 0 
while x <= y:
    if x % p != 0:
        print(x, end=' ')
        x += 1
    else:
        x += 11
        if x > y or x % p == 0:
            break
        print(x, end=' ')
        x += 1
    count += 1
    if count > 9:
        print("")
        count = 0
print("")
    # while x < p-10:
    #     print(*range(x,x+10))
    #     x += 10

    # while x % p == 0 and x < p:
    #     print(x, end='')
    #     x += 11

    # for i in range(x,x+11):
    #     print(*)