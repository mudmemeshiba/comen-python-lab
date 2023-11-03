def list_factors(n):
    int_factors = []
    factor = 1
    while factor <= n:
        if n % factor == 0:
            int_factors.append(factor)
        factor += 1
    str_factors = ' '.join(map(str, int_factors))
    # factors = list(map(int, l_factor.split()))
    return str_factors # return string of factors

def find_sum_and_num_factors(n):
    res = list_factors(n).split()
    int_factors = [int(i) for i in res]
    print("int factors")
    print(int_factors)
    sumFac = sum(int_factors)
    count = len(int_factors)
    return sumFac, count

def isPrime(number):
    if number == 1 or (number != 2 and number % 2 == 0):
        return False
    elif number == 2 or number == 3:
        return True
    else:
        div = 3
        count = 0
        while div < number:
            if number % div == 0:
                count += 1
            div += 2
        if count < 1:
            return True
        else:
            return False

n = int(input("Enter positive number: "))
print(f"Factors of {n} are")
print(list_factors(n))
sumNum = find_sum_and_num_factors(n)
print(f"Sum of {list_factors(n)} is {sumNum[0]}")
print(f"Number of factors is {sumNum[1]}")
if isPrime(n) == False:
    print(f"{n} is not prime number.")
else:
    print(f"{n} is prime number.")
