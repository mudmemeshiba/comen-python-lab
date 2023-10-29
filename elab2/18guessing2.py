target = 72
guess = int(input("Enter your guess (0 - 100): ")) 
if guess < 0 or guess > 100:
    print("Sorry, out of range, try again later.")
if guess >= 0 and guess < target:
    print("Sorry, your guess is too low, try again later.")
if guess > target and guess <= 100:
    print("Sorry, your guess is too high, try again later.")
if guess == target:
    print("Congratulations, your guess is correct.")