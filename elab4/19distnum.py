def count_digits(number):
    number = abs(number)
    count = 1
    mul = 10
    while abs(number//mul) != 0:
        count += 1
        mul *= 10
    return count

def get_last_digit(n):
	digits = []
	for i in range(count):
		digit = n % 10
		digits.append(digit)
		n = n // 10
	return digits	

#string join
def get_distribution(num):
	digits = get_last_digit(num)
	l_dist = []
	for i in range(count):
		l_dist.append(f"{digits[i]}x10^{i}")
		i += 1
		dist = ' + '.join(l_dist)
	return f"{num} = {dist}"

#main
num = int(input("Input number: "))
count = count_digits(num)
print(get_distribution(num))