def leapYear(y):
    if y%4 == 0 and (y%100 != 0 or y%400==0):
        return True
    else:
        return False

def days(d, m, y):
    days = d
    for i in range(m):
        if i in [1,3,5,7,8,10,12]:
            days += 31
        elif i in [4,6,9,11]:
            days += 30
        elif i == 2:
            if leapYear(y) == True:
                days += 29
            else:
                days += 28
    return days
d = int(input("d: "))
m = int(input("m: "))
y = int(input("y: "))
print(days(d, m, y))