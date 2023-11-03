size = int(input("input: "))
store = size

for i in range((size//2)+1):
    print(" "*(size//2) + "#"*((i*2)+1) + " "*(size//2))
    size -= 2

size = store
for i in range(size//2):
    print(" "*(i+1) + "#"*(size-2) + " "*(i+1))
    size -= 2