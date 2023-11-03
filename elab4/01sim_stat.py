def readNum():
    res = []
    while True:
        s = input("Enter a number (or [Enter] to exit): ")
        if s == '':
            break
        num = float(s)
        res.append(num)
    return res

sequence = readNum()
if sequence != []:
    print(f"The maximum is {max(sequence):.2f}")
    print(f"The minimum is {min(sequence):.2f}")
    print(f"The average is {(sum(sequence)/len(sequence)):.2f}")
else:
    print(f"Nothing to do.")