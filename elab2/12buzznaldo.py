total = int(input("How long have Buzz played ?: "))
hour  = total // 60
min   = total % 60
if min > 20:
    hour += 1
else:
    price = 0
if hour < 2:
    price = hour*900
elif hour >=2 and hour < 4:
    price = (hour*900)*0.9
elif hour == 4:
    price = (hour*900)*0.8
else:
    price = (hour*900)*0.7
print(f"Total price is {round(price)} baht.")