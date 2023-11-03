def readNum():
    res = []
    while True:
        s = input("Enter score (or ENTER to end): ")
        if s == '':
            break
        num = int(s)
        res.append(num)
    return res

def average():
    return sum(score)/len(score)

def standard_deviation():
    sd = []
    for i in range(len(score)):
        sd.append((score[i]-average)**2)
    return (sum(sd)/(len(score)-1))**0.5

def grade(score):
    # grade = 0
    if score >= average + (1.5*sd):
        grade = 'A'
    elif average + sd <= score < average + (1.5*sd):
        grade = 'B+'
    elif average + (0.5*sd) <= score < average + sd:
        grade = 'B'
    elif average <= score < average + (0.5*sd):
        grade = 'C+'
    elif average - (0.5*sd) <= score < average:
        grade = 'C'
    elif average - sd <= score < average - (0.5*sd):
        grade = 'D+'
    elif average - (1.5*sd) <= score < average - sd:
        grade = 'D'
    elif score < average - (1.5*sd):
        grade = 'F'
    return grade

score = readNum()
average  = average()
sd  = standard_deviation()
print(f"Average score is {average:.2f}")
print(f"Standard deviation is {sd:.2f}")

for i in range(len(score)):
    print(f"Student #{i+1} score: {score[i]} grade: {grade(score[i])}") 