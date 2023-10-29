buffet = input("Enter your buffet choice: ")
if buffet != "Korean" and buffet != "Japanese":
    print(f"Sorry, there is no {buffet} buffet.")
else: 
    wed    = input("Is today Wednesday (yes/no)? ")
    if buffet == "Japanese":
        if wed == "yes":
            print("Your payment is 850.00 Baht.")
        else:
            print("Your payment is 1000.00 Baht.")
    elif wed == "yes":
        print("Your payment is 1275.00 Baht.")
    else:
        print("Your payment is 1500.00 Baht.")