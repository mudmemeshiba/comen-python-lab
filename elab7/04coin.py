class Coin:
    def __init__(self, coin=1):
        self.coin = coin
    def __str__(self):
        return f'{self.coin} Baht Coin'

class BankNote:
    def __init__(self, value = 20):
        self.value = value
    def __str__(self):
        return f'{self.value} Baht Banknote'

class Application:
    def __init__(self, value=[1000, 500, 100, 50, 20, 10, 5, 2, 1]):
        self.amount = int(input("Input amount : "))
        self.value = value    

    def __str__(self):
        result = []
        for i in self.value:
            if self.amount >= i:
                if self.amount >= 20:
                    change = self.amount // i
                    self.amount -= (change * i)
                    result.append(f'You get {change} of {BankNote(i)}')
                else:
                    change = self.amount // i
                    self.amount -= (change * i)
                    result.append(f'You get {change} of {Coin(i)}')
        return "\n".join(result)
print(Application())
