weight = int(input("Weight: "))
height = int(input("Height: "))
BMI = round(weight/((height/100)**2), 1)
if BMI < 18.6:
    print(f"Your BMI is {BMI} You're in the underweight range.")
elif BMI >= 18.6 and BMI < 25:
    print(f"Your BMI is {BMI} You're in the healthy weight range.")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is {BMI} You're in the overweight range.")
else: 
    print(f"Your BMI is {BMI} You're in the obese range.")