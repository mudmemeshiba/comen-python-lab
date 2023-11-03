def draw(n):
    s = n #store
    for i in range(n-1):
        print(" "*i + "*" + " "*(s+((n-2)*2)) + "*")
        n -= 1

    n = s
    print(" "*(n-1) + "*"*n)
    for i in range(n-2):
        print(" "*(n-1) + "*" + " "*(n-2) + "*")
    print(" "*(n-1) + "*"*n)

    for i in range(n-1):
        print(" "*(s-(i+2)) + "*" + " "*(s+(i*2)) + "*")
        n += 1

n = int(input())
draw(n)

# 2 5 8 11
# 3n - 1

# 2:  2
# 3:  5 3
# 4:  8 6 4 
# 5: 11 9 7 5

# def draw(n):
#     sun = ""
#     s = n #store
#     for i in range(n-1):
#         sun += " "*i + "*" + " "*(s+((n-2)*2)) + "*" + "\n"
#         n -= 1

#     n = s
#     sun += " "*(n-1) + "*"*n + "\n"
#     for i in range(n-2):
#         sun += " "*(n-1) + "*" + " "*(n-2) + "*" + "\n"
#     sun += " "*(n-1) + "*"*n + "\n"

#     for i in range(n-1):
#         sun += " "*(s-(i+2)) + "*" + " "*(s+(i*2)) + "*"
#         if i < s-2:
#             sun += "\n"
#         n += 1
#     return sun

# n = int(input())
# print(draw(n))