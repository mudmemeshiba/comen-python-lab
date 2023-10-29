while True:
    num = int(input("Input number: ")) 
    if num % 2 == 0:
        print("Please input odd number")
    if num % 2 != 0:
        break

text = "x"
store = 1
for i in range(num):
    while store <= num:
        print(text*store)
        store += 1
store = num-1
while store != 0:
    print(text*store)
    store -= 1