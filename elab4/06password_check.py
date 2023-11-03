count = 0
while True:
    count += 1
    password = input("Enter your password: ")
    if password != "Programming is fun":
        print(f"Wrong password, attempt #{count}")
        print("Access not allowed")
    if count >= 3:
        print("Maximum attempts exceeded")
        break
    elif password == "Programming is fun":
        print("Correct password" + "\n" + "Access granted")
        break