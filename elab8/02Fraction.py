class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def evaluate(self):
        return self.numerator / self.denominator
    
    def add(self, n):
        return Fraction(self.numerator + (n * self.denominator), self.denominator)

    def __add__(self, frac):
        return Fraction((self.numerator * frac.denominator) + (frac.numerator * self.denominator), self.denominator * frac.denominator)

    def multiply(self, n):
        self.numerator *= n
        return self

    def __mul__(self, other):
        return Fraction((self.numerator * other.numerator), (self.denominator*other.denominator))
    
    def __str__(self):
        div = gcd(self.numerator, self.denominator)
        num = int(self.numerator / div)
        den = int(self.denominator / div)
        return f"{num} / {den}"
    
def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

print(Fraction(-5,2))
print((Fraction(1,2) + Fraction(3,4)).multiply(0))
print((Fraction(22,14) * Fraction(2, 4)).add(1))
print(Fraction(22, 7).multiply(7).multiply(7))

class A:
    x: int

    def __init__(self, x) -> None:
        self.x = x

    # method
    def f(self):
        print(self.x)

b = A(1)
b.f()