age = int(input("Enter your age : "))
if age >= 0 and age <= 12:
    print("You are Child.")
elif age >= 12 and age <= 18:
    print("You are Adolescence.")
elif age >= 19 and age <= 59:
    print("You are Adult.")
else:
    print("You are Senior Adult.")