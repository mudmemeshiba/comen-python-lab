def readNum():
    res = []
    while True:
        s = input("Enter a number (or zero to exit): ")
        if s == '' or s == '0':
            break
        num = float(s)
        res.append(num)
    return res

sequence = readNum()
pos = []
neg = []
for num in sequence:
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)
print(f"The sum of all positive numbers is {sum(pos):.2f}")
print(f"The sum of all negative numbers is {sum(neg):.2f}")