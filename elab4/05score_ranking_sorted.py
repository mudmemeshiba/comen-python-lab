def readNum():
    res = []
    while True:
        s = input("Enter score (or ENTER to end): ")
        if s == '':
            break
        num = int(s)
        res.append(num)
    return res

score = readNum()
score_sorted = sorted(score, reverse=True)

for i in range(len(score)):
    print(f"Rank #{i+1}: {score_sorted[i]}")