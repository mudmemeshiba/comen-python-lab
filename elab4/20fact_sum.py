def factorial(x):
    fact = 1
    while x >= 1:
        fact = fact * x
        x -= 1
    return fact

k = int(input("Input k: "))
sum = 0
for i in range(k):
    sum += factorial(i+1)
    print(f"{i+1}! = {factorial(i+1)}")
print(f"Summation of factorial 1!-{k}! = {sum}")