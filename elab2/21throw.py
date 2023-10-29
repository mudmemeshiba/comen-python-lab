min  = int(input("Minutes before due: "))
temp = float(input("Temperature: "))
rain = input("Is it raining (y/n)? ")

if min >= 720 and min <= 1440:
    day = 1
elif min >= 1440 and min % 1440 >= 720 :
    day = (min//1440)+1
else:
    day = min//1440
print(f">>> {day} days before due.")

if day > 5:
    print(">>> I will not do the assignment.")
elif day >= 2 and (temp > 40 or (temp > 25 and (rain == "y" or rain == "Y"))):
    print(">>> I will not do the assignment.")
elif day < 2:
    print(">>> I will do the assignment.")
else:
    print(">>> I will do the assignment.")