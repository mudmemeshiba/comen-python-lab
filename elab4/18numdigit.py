def count_digits(number):
    number = abs(number)
    count = 1
    mul = 10
    while abs(number//mul) != 0:
        count += 1
        mul *= 10
    return count

# Main
number = int(input("Enter number: "))
print(f"There are {count_digits(number)} digits in {number}")