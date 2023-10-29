tv    = int(input("How many TVs? "))
dvd   = int(input("How many DVD players? "))
audio = int(input("How many Audio Systems? "))
price = (tv*6000) + (dvd*1500) + (audio*3000)
print(f"Total price is {price:.2f} baht.")
if price >= 24000:
    print(f"You've got a discount of {(price*0.2):.2f} baht.")
    print(f"Your payment is {(price*0.8):.2f} baht. Thank you!")
else:
    print(f"Your payment is {price:.2f} baht. Thank you!")