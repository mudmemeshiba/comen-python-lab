rc   = int(input('Enter the number of rows or columns : '))
grid = []
n    = 1

for i in range(rc):
    for j in range(rc):
        grid.append('%2d' % n) #as string
        # grid.append(n) #as int 
        n += 1
    n -= rc-1

for i in range(rc):
    print(" ".join(grid[i*rc : (i+1)*rc]))