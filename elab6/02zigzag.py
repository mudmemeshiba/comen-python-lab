sentence = input("Input sentence: ")
row = int(input("Input row: "))
grid = []

for i in range(row):
    grid.append([])

n = 0
count = 0
while n < len(sentence):
    for i in range(row):
        if count % (row-1) == 0:
            grid[i].append(sentence[n])
            n += 1 
        elif count == row - (count % (row-1))-1:
            grid[i].append(sentence[n])
            n += 1
        else:
            grid[i].append([])
    count += 1

for i in range(row):
    print(grid[i])


# for i in range(row):
#     print(''.join(grid[i]))

# count 0 row 1

# for i in range(len(grid[[0]])*row):



# for i in range(row):
#     print(" ".join(grid[i]))

# newSentence = ""
# for i in range(row):
#     for j in range(row):
#         newSentence += "".join(grid[j][i])
# print(newSentence)