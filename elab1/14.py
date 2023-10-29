dividend  = int(input("Input Dividend: "))
divider   = int(input("Input Divider: "))
quotient  = dividend // divider
remainder = dividend % divider
print(f"{dividend} = {divider} * {quotient} + {remainder}")