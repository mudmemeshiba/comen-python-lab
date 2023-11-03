# A = [[1,2,3],[4,5,6],[7,8,9]]
# B = [[22,13,23],[54,43,21],[23,78,71]]
# A = [[1,2,3],[4,5,6]]
# B = [[2,3],[4,5],[6,7]]
A = [[8, 10], [12, 14], [16, 18]]
B = [[279, 356], [415, 396]]

def mul_matrix(A, B):
    zero = []
    for i in range(len(A)):
        subzero = []
        for _ in range(len(B[0])):
            subzero.append(0)
        zero.append(subzero)
    print(zero)

    for i in range(len(A)):
        for j in range(len(A[i])):
            for k in range(len(B[j])):
                zero[i][k] += A[i][j] * B[j][k]
    return zero

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()

# mul_matrix(A, B)
print_matrix(mul_matrix(A,B))