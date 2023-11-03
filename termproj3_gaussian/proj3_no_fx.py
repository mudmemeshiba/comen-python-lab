def readMatMod(fn):
    m = []
    with open(fn) as fp:
        for line in fp:
            row = []
            for n in line.strip().split(' '):
                row.append(Fraction(int(n)))
            m.append(row)
    return m

def printMatMod(m):
    for i in range(len(m)):
        row = ''
        for j in range(len(m[0])):
            row += f'{str(m[i][j]):^8}'
        print(row)
    print()
   
class Fraction:
    def __init__(self, numerator, denominator=1):
        gcd_denom = gcd(numerator, denominator)
        self.numerator = int(numerator // gcd_denom)
        self.denominator = int(denominator // gcd_denom)

    def evaluate(self):
        return self.numerator / self.denominator
    
    def add(self, n):
        return Fraction(self.numerator + (n * self.denominator), self.denominator)

    def __add__(self, frac):
        return Fraction((self.numerator * frac.denominator) + (frac.numerator * self.denominator), self.denominator * frac.denominator)

    def __sub__(self, frac):
        return Fraction((self.numerator * frac.denominator) - (frac.numerator * self.denominator), self.denominator * frac.denominator)

    def multiply(self, n):
        self.numerator *= n
        return self
    
    def __mul__(self, other):
        return Fraction((self.numerator * other.numerator), (self.denominator * other.denominator))
    
    def __truediv__(self, other):
        return Fraction((self.numerator * other.denominator), (self.denominator * other.numerator))

    def __repr__(self):
        num = int(self.numerator)
        den = int(self.denominator)
        if den == 1:
            return f"{num}"
        else:
            return f"{num}/{den}"

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def minusRow(matrix, row, diag, j):
    for i in range(len(row)):
       matrix[j][i] = row[i] - diag[i]
    return matrix

def divRow(row, div):
    newRow = []
    for i in range(len(row)):
        newRow.append(row[i]/div)
    return newRow

def printRow(row):
    c = 0
    print("[", end='')
    for i in row:
        if c == len(row)-1:
            print(i, end='')
        else:
            print(i, end=', ')
        c += 1
    print("]")

def gaussian(matrix):
    for i in range(len(matrix)-1):
        print(f"R{i+1}->R{i+1}/({matrix[i][i]})", end=' ')
        diag = divRow(matrix[i], matrix[i][i])
        printRow(diag)
        for j in range(len(matrix[i])-1):
            if j > i and matrix[j][i].evaluate() != 0:
                print(f"R{j+1}->R{j+1}/({matrix[j][i]})", end=' ')
                row = divRow(matrix[j], matrix[j][i])
                printRow(row)
                print(f"R{j+1} ==> R{j+1} - R{i+1}")
                minusRow(matrix, row, diag, j)
                printMatMod(matrix)

    for i in range(len(matrix)):
        if matrix[i][i].evaluate() != 1:
            print(f"R{i+1} ==> R{i+1} / ({matrix[i][i]})")
            matrix[i] = divRow(matrix[i], matrix[i][i])
    printMatMod(matrix)

    print("Result from Gaussian Elimination:")
    printMatMod(matrix)
    return matrix

def backSub(matrix):
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y', 'z']
    ans = [0] * len(matrix)
    print("After Back-Substitution:")
    for i in range(len(matrix)-1, -1, -1):
        res = matrix[i][-1]
        for j in range(i + 1, len(matrix)):
            res = res - (matrix[i][j] * ans[j])
        ans[i] = res
    
    for i in range(len(ans)):
        print(f"{char[i]} = {ans[i]}")

fn = input("Enter filename: ")
matrix = readMatMod(fn)
print("Augmented matrix:")
printMatMod(matrix)
matrix = gaussian(matrix)
backSub(matrix)