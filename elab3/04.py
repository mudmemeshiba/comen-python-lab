# def check_prime(n):
#     while True:
#         if n == 2 or n == 3:
#             return True
#         elif n <= 1 or n % 2 == 0:
#             break
#         else:
#             i = 3
#             while n > i:
#                 if n % i == 0:
#                    return False
#                 elif n % i != 0:
#                     i += 2
#             return True

    # if check_prime(n) == True:
    #     return 2
def factor_count(n):
    count = 0
    div = 1
    while n >= div:
        if n % div == 0:
            count += 1
        div += 1
    return count

n = int(input("Enter n: "))
c = factor_count(n)
print(c)