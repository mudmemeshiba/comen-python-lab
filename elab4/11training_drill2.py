day = int(input("Day: "))
l_day = []
i, j = 1, 1
if day <= 2:
    for _ in range(day):
        l_day.append(i)
else:
    l_day = [1, 1]
    for _ in range(day-2):
        k = i + j
        j = i
        i = k
        l_day.append(i)
print(*l_day)