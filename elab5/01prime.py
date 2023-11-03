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

def printAllPrimes(limit):
    for i in range(limit+1):
        if isPrime(i) == True:
            print(i, end=" ")

number = int(input("Input n: "))
print(isPrime(number))
printAllPrimes(number)