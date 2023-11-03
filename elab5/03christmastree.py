# announce global var 

level = int(input("How many levels? "))
size  = int(input("Enter size of each bush: "))

store = size
ast = 1
for a in range(level):
    for b in range(size):
        print(" "*(size-1) + "*"*(ast))
        ast += 2
        size -= 1
        # reset var
    size = store
    ast = 1

# for a in range(level):
#     for b in range(size):
#         print(" "*(size-1), end='')
#         print("*"*(ast), end='')
#         print(" "*(size-1), end='')
#         print()
#         ast += 2
#         size -= 1
#     size = store
#     ast = 1

#   *     (2+1+2)
#  ***    (1+3+1)
# *****   (0+5+0)