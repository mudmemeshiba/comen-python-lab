# num = int(input())
# store = 1
# for i in range(num):
#     if num == 1:
#         print(1)
#     elif num > i+1:
#         print(store, store+1)
#         i += 1

num = int(input("Input number: "))
store = 1
for i in range(num):
    while store <= num:
        print(*range(1, store+1))
        store += 1
