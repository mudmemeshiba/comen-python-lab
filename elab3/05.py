def fibo(n):
    if n == 1 or n ==2:
        return 1
    n1, n2 = 1, 1
    i = 1
    while i <= n-2:
        new   = n1 + n2
        n1,n2 = n2,new
        i += 1
    return new
n = int(input("Enter n: "))
print("fibo({}) = {}".format(n, fibo(n)))

    # for i in range(n-2):
    #     new = n1 + n2
    #     n1,n2 = n2,new
    # return new

# 0 1 2 3 4 5 6  7  8
# 0 1 1 2 3 5 8 13 21
        
# n = int(input("Enter n: "))
# print(fibo(n))

# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     # elif n > 2:
#     #     return fibo(n-1) + fibo(n-2)
#     n1, n2 = 1, 1
#     i = 3
#     while i <= n-2:
#         n = n1 + n2
#         n1, n2 = n2, n
#         i += 1
#     return fibo
        
# n = int(input("Enter n: "))
# print("My name is {0}, I'm {1}".format("John",36))
# print(fibo(n))
# # print("fibo({}) = {}".format(n, fibo(n)))
# # print(f"fibo({n}) = {fibo(n)}")