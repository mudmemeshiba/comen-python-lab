msg = input("Enter a message: ")
space = 0
for i in range(len(msg)):
    print(f"{' '*space}{msg[i]}")
    space += 1