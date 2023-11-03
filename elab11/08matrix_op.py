A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
D = [[100,50],[20,70]]
c = 2

def transpose_matrix(A):
    matrixT = []
    for i in range(len(A[0])):
        row = []
        for j in range(len(A)):
            row.append(A[j][i])
        matrixT.append(row)
    return matrixT

def plus_matrix(A, B):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = A[i][j]+B[i][j]
    return A

def minus_matrix(A, B):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = A[i][j]-B[i][j]
    return A

def mul_matrix(A, B):
    zero = []
    for i in range(len(A)):
        subzero = []
        for _ in range(len(B[0])):
            subzero.append(0)
        zero.append(subzero)

    for i in range(len(A)):
        for j in range(len(A[i])):
            for k in range(len(B[j])):
                zero[i][k] += A[i][j] * B[j][k]
    return zero

def power_matrix(A, c):
    B = A
    for _ in range(c-1):
        B = mul_matrix(A, B)
    return B

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()

def matrix_op(A, B, C, D, c):
    bT = transpose_matrix(B)
    cP = power_matrix(C, c)
    first = plus_matrix(A, bT)
    second = minus_matrix(cP, D)
    res = mul_matrix(first, second)
    return res

print_matrix(matrix_op(A, B, C, D, c))