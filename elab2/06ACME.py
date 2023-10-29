buy = float(input("Enter buying amount: "))
if buy >= 1000 and buy < 3000:
    print(f"Amount due after discount is {(buy*0.9):.2f} baht.")
elif buy >= 3000:
    print(f"Amount due after discount is {(buy*0.85):.2f} baht.")
else:
    print(f"Amount due after discount is {(buy):.2f} baht.")