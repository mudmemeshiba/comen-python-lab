direction = input("Direction to flip square (V/H): ")
size = int(input("Input size of square: "))
store = size
matrix = []
flip = []

for i in range(size):
    row = input()
    matrix.append(row.split())

if direction == "V" or direction == "v":
    for i in range(size):
        for j in range(size):
            flip.append(matrix[store-1][j])
        store -= 1
else:
    for i in range(size):
        for _ in range(size):
            flip.append(matrix[i][size-1])
            size -= 1
        size = store

print(flip)
print("After flip:")
for i in range(size):
    print(" ".join(flip[i*size : (i+1)*size]))

print(" ".join(flip[i:size])) # prints triangle

# [x:y]

# print(matrix)
# print(matrix[0][0])
# print(matrix[1][0])
# print(matrix[2][0])
# print(matrix[3][0])
