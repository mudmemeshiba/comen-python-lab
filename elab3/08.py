def distance(acceleration,time):
    return 1/2*acceleration*(time**2)

acceleration = int(input("Acceleration : "))
time = int(input("Time : "))
print(distance(acceleration,time))