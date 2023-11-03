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

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()

print_matrix(plus_matrix(A,B))