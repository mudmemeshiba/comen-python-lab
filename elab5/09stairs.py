def draw(m):
    for i in range(len(m)):
        print(str(m[i])*(i+1))

m = input("")
while m != "0":
    m = [str(i) for i in m.split()]
    draw(m)
    m = input("")
print("Good Bye.")