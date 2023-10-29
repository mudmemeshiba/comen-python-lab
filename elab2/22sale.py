day = int(input("How many day : "))
percent = 5
sum     = 0
for i in range(day):
    price = float(input(f"Input price in day {i+1} : "))
    sum += price*(1-(percent/100))
    percent += 1
print(f"Summary price = {sum:.2f}")