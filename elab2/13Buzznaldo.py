inj = input("Is Bulotelli injured?(y/n) ")
if inj == "y":
    print("Not available")
else:
    late = input("Is Bulotelli late for the training?(y/n) ")
    if late == "n":
        print("Starter")
    else:
        well = input("Did Bulotelli perform well in training?(y/n) ")
        if well == "y":
            print("Substitute")
        else:
            print("Not selected")