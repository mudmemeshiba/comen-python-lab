n = int(input("N: "))
m = int(input("M: "))
resList = []
for i in range(n):
    mod = int(input(f"Input number {i+1}: "))
    res = mod % m
    if res not in resList:
        resList.append(res)
print(len(resList))