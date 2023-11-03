def al_sum(n):
    if n == 1:
        sum = 1
    elif n % 2 == 0:
        sum = int((n/2)*-1)
    elif n % 2 != 0:
        sum = int(n/2)+1
    return sum

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n, al_sum(n)))

# n = int(input("Enter n of series: "))
# al_sum = int((n/2)*-1)
# if n % 2 == 0:
#     print(f"Alternating Sum from 1 to {n} is {al_sum}")
# else:
#     print(f"Alternating Sum from 1 to {n} is {round(n/2)}")