import math

def find_cylinder_volume(r, h):
    # V = math.pi * pow(r, 2) * h
    # return V
    return math.pi * (r**2) * h

r = float(input("radius = "))
h = float(input("height = "))
V = find_cylinder_volume(r, h)

print(V)
print("Volume = %.2f" %V)