m, n  = map(int, input("Grid Size: ").split())
mines = int(input("Number of mine(s): "))
mine_sweeper = []
for i in range(n):
    mine_sweeper.append([0]*m)

for i in range(mines):
    print((f"Mine#{i+1}: "), end='')
    x, y = map(int, input().split())
    mine_sweeper[y][x] = "X"

for i in range(n):
    for j in range(m):
        if mine_sweeper[i][j] == "X": 
            if 0 <= j+1 < m and mine_sweeper[i][j+1] != "X": #east
                mine_sweeper[i][j+1] += 1
            if 0 <= j-1 < m and mine_sweeper[i][j-1] != "X": #west
                mine_sweeper[i][j-1] += 1
            if 0 <= i-1 < n and mine_sweeper[i-1][j] != "X": #north
                mine_sweeper[i-1][j] += 1
            if 0 <= i+1 < n and mine_sweeper[i+1][j] != "X": #south
                mine_sweeper[i+1][j] += 1

            if 0 <= i-1 < n and 0 <= j+1 < m and mine_sweeper[i-1][j+1] != "X": #NE
                mine_sweeper[i-1][j+1] += 1
            if 0 <= i-1 < n and 0 <= j-1 < m and mine_sweeper[i-1][j-1] != "X": #NW
                mine_sweeper[i-1][j-1] += 1
            if 0 <= i+1 < n and 0 <= j+1 < m and mine_sweeper[i+1][j+1] != "X": #SE
                mine_sweeper[i+1][j+1] += 1
            if 0 <= i+1 < n and 0 <= j-1 < m and mine_sweeper[i+1][j-1] != "X": #SW
                mine_sweeper[i+1][j-1] += 1
for i in range(n):
    print(*mine_sweeper[i]) 

print(mine_sweeper)

#list of string
# for i in range(m*n):
#     mine_sweeper.append(f"{i}")
# count = 0
# for i in range(n):
#     print(' '.join(mine_sweeper[count:count+3])) 
#     count += 3
