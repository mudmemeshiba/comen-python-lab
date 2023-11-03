duration = []
dead = 0
totalTime = 1

n, m = [int(i) for i in input().split()]
for i in range(n):
    duration.append(int(input()))

while dead < m:
    for i in range(len(duration)):
        if totalTime % duration[i] == 0:
            dead += 1
    totalTime += 1
print(totalTime-1)