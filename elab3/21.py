import math

def nb_year(p0, percent, aug, p):
    day = 0
    while p0 < p:
        p0 = p0 + (p0*(percent/100)) + aug
        p0 = math.floor(p0)
        day += 1
    return day

print(nb_year(1000, 2, 30, 1150))
print( nb_year(1500000, 0.25, 1000, 2000000) )