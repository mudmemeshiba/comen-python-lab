# A = [[1,2],[3,4],[5,6]]
# B = [[7,9,11],[8,10,12]]
# C = [[13,14],[15,16]]
# c = 2
A = [[1,2],[3,4],[5,6]] 

def transpose_matrix(A):
    matrixT = []
    for i in range(len(A[0])):
        row = []
        for j in range(len(A)):
            row.append(A[j][i])
        matrixT.append(row)
    return matrixT

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()

print_matrix(transpose_matrix(A))

# import numpy as np
# A = np.array([[1,2],[3,4],[5,6]])
# print(A)
# [[1 2]
#  [3 4]
#  [5 6]]
# print(A.T)
# [[1 3 5]
#  [2 4 6]]