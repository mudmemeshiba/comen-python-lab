size = int(input(""))
arena = []
bomb = 0

for i in range(size):
    arena.append(list(input()))

for i in range(size):
    for j in range(size):
        if arena[i][j] == "G":
            # E-W
            if 0 <= j+2 < size and arena[i][j+2] == "E":
                bomb += 1
                arena[i][j+2] = "X"
            if 0 <= j+1 < size and arena[i][j+1] == "E":
                bomb += 1
                arena[i][j+1] = "X"
            if 0 <= j-1 < size and arena[i][j-1] == "E":
                bomb += 1
                arena[i][j-1] = "X"
            if 0 <= j-2 < size and arena[i][j-2] == "E":
                bomb += 1
                arena[i][j-2] = "X"
            
            # S-N
            if 0 <= i+2 < size and arena[i+2][j] == "E":
                bomb += 1
                arena[i+2][j] = "X"
            if 0 <= i+1 < size and arena[i+1][j] == "E":
                bomb += 1
                arena[i+1][j] = "X"
            if 0 <= i-1 < size and arena[i-1][j] == "E":
                bomb += 1
                arena[i-1][j] = "X"
            if 0 <= i-2 < size and arena[i-2][j] == "E":
                bomb += 1
                arena[i-2][j] = "X"
            
            # Diagonal topLeft -> bottomRight
            if 0 <= i-2 < size and 0 <= j-2 < size and arena[i-2][j-2] == "E":
                bomb += 1
                arena[i-2][j-2] = "X"
            if 0 <= i-1 < size and 0 <= j-1 < size and arena[i-1][j-1] == "E":
                bomb += 1
                arena[i-1][j-1] = "X"
            if 0 <= i+1 < size and 0 <= j+1 < size and arena[i+1][j+1] == "E":
                bomb += 1
                arena[i+1][j+1] = "X"
            if 0 <= i+2 < size and 0 <= j+2 < size and arena[i+2][j+2] == "E":
                bomb += 1
                arena[i+2][j+2] = "X"
            
            # Diagonal topRight -> bottomLeft
            if 0 <= i-2 < size and 0 <= j+2 < size and arena[i-2][j+2] == "E":
                bomb += 1
                arena[i-2][j+2] = "X"
            if 0 <= i-1 < size and 0 <= j+1 < size and arena[i-1][j+1] == "E":
                bomb += 1
                arena[i-1][j+1] = "X"
            if 0 <= i+1 < size and 0 <= j-1 < size and arena[i+1][j-1] == "E":
                bomb += 1
                arena[i+1][j-1] = "X"
            if 0 <= i+2 < size and 0 <= j-2 < size and arena[i+2][j-2] == "E":
                bomb += 1
                arena[i+2][j-2] = "X"
            
            # Else on W side
            if 0 <= i-2 < size and 0 <= j-1 < size and arena[i-2][j-1] == "E":
                bomb += 1
                arena[i-2][j-1] = "X"
            if 0 <= i-1 < size and 0 <= j-2 < size and arena[i-1][j-2] == "E":
                bomb += 1
                arena[i-1][j-2] = "X"
            if 0 <= i+1 < size and 0 <= j-2 < size and arena[i+1][j-2] == "E":
                bomb += 1
                arena[i+1][j-2] = "X"
            if 0 <= i+2 < size and 0 <= j-1 < size and arena[i+2][j-1] == "E":
                bomb += 1
                arena[i+2][j-1] = "X"
            
            # Else on E side
            if 0 <= i-2 < size and 0 <= j+1 < size and arena[i-2][j+1] == "E":
                bomb += 1
                arena[i-2][j+1] = "X"
            if 0 <= i-1 < size and 0 <= j+2 < size and arena[i-1][j+2] == "E":
                bomb += 1
                arena[i-1][j+2] = "X"
            if 0 <= i+1 < size and 0 <= j+2 < size and arena[i+1][j+2] == "E":
                bomb += 1
                arena[i+1][j+2] = "X"
            if 0 <= i+2 < size and 0 <= j+1 < size and arena[i+2][j+1] == "E":
                bomb += 1
                arena[i+2][j+1] = "X"
print(bomb)
for i in range(size):
    print(*arena[i]) 
