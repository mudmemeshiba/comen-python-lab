def check_prime(n):
    while True:
        if n == 2 or n == 3:
            return True
        elif n <= 1 or n % 2 == 0:
            break
        else:
            i = 3
            while n > i:
                if n % i == 0:
                   return False
                elif n % i != 0:
                    i += 2
            return True
            

n = int(input("Enter number: "))
if check_prime(n):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")