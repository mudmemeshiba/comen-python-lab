x  = int(input("x: "))
op = input("Operator: ")
y  = int(input("y: "))
if op == "+":
    print(x+y)
elif op == "-":
    print(x-y)
elif op == "*":
    print(x*y)
elif op == "/":
    print(f"{(x/y):.2f}")
elif op == "%":
    print(x%y)
else:
    print("Unknown Operator")