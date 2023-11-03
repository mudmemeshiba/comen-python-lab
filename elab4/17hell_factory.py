def BECKS(A, B, C):
    total = A+B+C
    while total > 1:
        A, B, C = compare(A, B, C)
        total -= 1
# find a way to write 'if ... == 1, return ...
    if A == 1:
        last = 'A'
    elif B == 1:
        last = 'B'
    else:
        last = 'C'
    return last

def compare(A, B, C):
    if A >= B >= C or B >= A >= C:
        A -= 1
        B -= 1
        C += 1
    elif B >= C >= A or C >= B >= A:
        A += 1
        B -= 1
        C -= 1
    elif A >= C >= B or C >= A >= B:
        A -= 1
        B += 1
        C -= 1    
    return A, B, C

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
print(BECKS(A, B, C))

# A A A A C C C B B
# A A A B   C C B B

    # if A not in comp:
    #     A += 1
    #     B -= 1
    #     C -= 1
    # elif B not in comp:
    #     B += 1
    #     A -= 1
    #     C -= 1
    # elif C not in comp:
    #     C += 1
    #     A -= 1
    #     B -= 1