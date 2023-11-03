import math

def MiniHeart(L):
    return ((math.pi*(L/2)**2)) + (L**2)

L = float(input("Please enter the value of L: "))
area = MiniHeart(L)
print(f"Area is {area:.4f}")