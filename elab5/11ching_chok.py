luckyNum  = int(input("Enter lucky number : "))
candidates = int(input("Enter amount of candidates : ")) 
idCard = []
occ = []
equalIndex = []

# idCard input
for i in range(candidates):
    ID = input(f"Enter ID card number {i+1}: ")
    idCard.append(ID)

# count lucky num's occurence(s) in each idCard
for i in range(candidates):
    count = 0
    for j in range(len(idCard[0])):
        if str(luckyNum) in idCard[i][j]:
            count += 1
    occ.append(count)

# check if there're same occ 
for i in range(len(occ)-1):
    if occ[i] == occ[i+1] and (occ[i] != 0 or occ[i+1] != 0):
        equalIndex.append(i)

# find winner
if len(equalIndex) == candidates-1 or occ.count(0) == candidates:
    winner = max(idCard)
elif equalIndex == []: # no same occ
    index = occ.index(max(occ))
    winner = idCard[index]
else: # compare which one is greater 
    max_occ_index = []
    for i, val in enumerate(occ):
        if val == max(occ):
            max_occ_index.append(i)
    winner = idCard[max_occ_index[0]]
    for i in max_occ_index:
        if int(idCard[i]) > int(winner):
            winner = idCard[i]
if winner != "":
    print(f"Winner: {winner}")

# max_occ_index = [i for i, val in enumerate(occ) if val == max(occ)]