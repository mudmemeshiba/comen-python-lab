def digit(n):
    if n < 10:
        return n
    else:
        return n % 10

def tens(n):
    if n >= 10:
        return ((n - (hundreds(n) * 100)) // 10) % 100
    else:
        return 0

def hundreds(n):
    if n >= 1000:
        return (n - (thousands(n) * 1000)) // 100
    else:
        return n // 100
    
def thousands(n):
    return n // 1000

def sum_digits(n):
    return digit(n) + tens(n) + hundreds(n) + thousands(n)

n = int(input('Enter a number (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % sum_digits(n))