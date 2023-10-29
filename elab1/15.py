x = int(input("x: "))
y = int(input("y: "))

hr_mod  = y % 24
hr_left = 24 - x
if (x + hr_mod > 24):
    time = abs(hr_mod-hr_left)
else:
    time = x + hr_mod
print(f"She comes at {time}:00")