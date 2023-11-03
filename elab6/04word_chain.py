words = input("Text: ").split()
chains = 0
length = 1
lengthList = []
for i in range(len(words)-1):
    diff = 0
    for j in range(len(words[i])):
        if words[i][j] != words[i+1][j]:
            diff += 1
        if diff > 2:
            chains += 1
            lengthList.append(length)
            length = 0
            break
        if i == len(words)-2 and j == len(words[i])-2 and diff <= 2:
            lengthList.append(length+1)
            length = 0
    length += 1
chains += 1
print(f"{chains} Chain(s). Maximum length is {max(lengthList)} word(s).")                    