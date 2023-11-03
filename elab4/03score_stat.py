def readNum():
    res = []
    while True:
        s = input("Enter score (or ENTER to end): ")
        if s == '':
            break
        num = int(s)
        res.append(num)
    return res

sequence = readNum()
count = 0
for student in sequence:
    print(f"Student #{count+1} score: {sequence[count]}")
    count += 1
print(f"Average score is {(sum(sequence)/len(sequence)):.2f}")
print(f"Minimum score is {min(sequence)}")
print(f"Maximum score is {max(sequence)}")