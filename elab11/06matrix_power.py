A = [[1,2,3],[4,5,6],[7,8,9]]
c = 2

def mul_matrix(A, B):
    zero = []
    for i in range(len(A)):
        subzero = []
        for j in range(len(B[0])):
            subzero.append(0)
        zero.append(subzero)
    
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            for k in range(len(B[i])):
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

print_matrix(power_matrix(A,c))