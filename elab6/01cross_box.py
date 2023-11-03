n = int(input())
x = (n-3)/2
times = int(x)
mid   = n-4

print("."*n)
for i in range(times):
    print("." + (" "*i) + "." + (" "*mid) + "." + (" "*i) + ".")
    mid -= 2
    
print("." + (" "*times) + "." + (" "*times) + ".")

space = 1
for i in range(times):
    print("." + (" "*(times-1)) + "." + (" "*space) + "." + (" "*(times-1) + "."))
    space += 2
    times -= 1
print("."*n)

# def firstHalf(times, mid):
#     print("."*n)
#     for i in range(times):
#         print("." + (" "*i) + "." + (" "*mid) + "." + (" "*i) + ".")
#         mid -= 2
    
# def middle(times):
#     print("." + (" "*times) + "." + (" "*times) + ".")

# def lastHalf(times, mid):
#     space = 1
#     for i in range(times):
#         print("." + (" "*(times-1)) + "." + (" "*space) + "." + (" "*(times-1) + "."))
#         space += 2
#         times -= 1
#     print("."*n)

# n = int(input())
# times = int((n-3)/2)
# mid   = n-4
# print(firstHalf(times, mid))
# print(middle(times))
# print(lastHalf(times, mid))

# HOW TO FIX RETURN NONE?????

# ..     ..  2     + 5 + 2
# . .   . .  1+1+1 + 3 + 1+1+1
# .  . .  .
# .   .   .
# .  . .  .
# . .   . .
# ..     ..

# 9-6  = 3
# 11-7 = 4
# 13-8 = 5
# 15-9 = 6

# 13 = x  + x + 3
# 13 = 2x + 3
# (13-3)/2 = x
# (n-3)/2  = x