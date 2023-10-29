a  = int(input("Input a: "))
b  = int(input("Input b: "))
c  = int(input("Input c: "))
d  = int(input("Input d: "))
e  = int(input("Input e: "))
u  = round(((a+b+c+d+e)/5), 3)
sd = ((((a-u)**2)+((b-u)**2)+((c-u)**2)+((d-u)**2)+((e-u)**2))/5)**0.5
print(f"mean: {u:.3f}")
print(f"sd: {sd:.3f}")