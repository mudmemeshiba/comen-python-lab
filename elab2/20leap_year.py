year = int(input("Enter year: "))
if year < 1:
    print( "Invalid year.")
elif year % 400 == 0:
    print(f"{year} is a leap year.")    
elif year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year.")
else: 
    print(f"{year} is not a leap year.")