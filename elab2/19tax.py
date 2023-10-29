age    = int(input("Enter your age: "))
income = int(input("Enter your net income: "))
if age < 15 or age > 60:
    print("Invalid age.")
elif income >= 1 and income <= 30000:
    print(f"Your negative income tax is {(income*0.2):.2f} Baht.")
elif income >= 30000 and income <= 79999:
    print(f"Your negative income tax is {((0.2*30000)-(0.12*(income-30000))):.2f} Baht.")
else:
    print("Invalid income.")