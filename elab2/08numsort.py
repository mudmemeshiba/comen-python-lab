num1 = int(input())
num2 = int(input())
num3 = int(input())
store = 0

if num1 > num3:
    store = num3
    num3  = num1
    num1  = store
# num1 < num3
# print(num1, num2, num3, store)

if num1 > num2:
    store = num2
    num2  = num1
    num1  = store

if num2 > num3:
    store = num3
    num3  = num2
    num2  = store
print(num1, num2, num3)
