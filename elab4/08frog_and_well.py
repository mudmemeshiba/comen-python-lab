depth = int(input("Enter the depth of the well: "))
jump  = int(input("Enter the height the frog can jump up: "))
slip  = int(input("Enter the height the frog slips down: "))
day = 1

if jump <= slip < depth:
    print("The frog cannot get out of the well.")
else:
    while depth-jump > 0:
        depth = depth-jump
        print(f"On day {day} the frog leaps to the depth of {depth} meters.")
        depth = depth+slip
        print(f"At night he slips down to the depth of {depth} meters.")
        day += 1
    print(f"The frog is free on day {day}.")
        
