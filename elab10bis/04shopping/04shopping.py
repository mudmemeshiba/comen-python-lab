import json

class Coin:
    def __init__(self, coin=1):
        self.coin = coin
    def __str__(self):
        return f'{self.coin}'

class BankNote:
    def __init__(self, value = 20):
        self.value = value
    def __str__(self):
        return f'{self.value}'

class Application:
    def __init__(self, value=[1000, 500, 100, 50, 20, 10, 5, 2, 1]):
        self.money = money
        self.value = value    

    def __str__(self):
        result = []
        for i in self.value:
            if self.money >= i:
                if self.money >= 20:
                    change = self.money // i
                    self.money -= (change * i)
                    result.append(f'{BankNote(i)} : {change}')
                else:
                    change = self.money // i
                    self.money -= (change * i)
                    result.append(f'{Coin(i)} : {change}')
        return "\n".join(result)

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

def shopping(data):
    priceList = []
    cust = []

    for value in data['products']:
        priceList.append(value)

    for value in data['customers']:
        cust.append([value.get('customer_name'), value.get('order'), value.get('money')])
    cust.sort()

    for detail in cust:
        name = detail[0]
        print(name)
        global price
        price = 0
        for key, value in detail[1].items():
            for product in priceList:
                if key == product['product_name']:
                    price += value * int(product['price'])
        change(name, cust, price)
        print()

def change(name, cust, price):
    
    for detail in cust:
        global money
        money = 0
        if name == detail[0]:
            money = detail[2]
            if money == price:
                print("No change")
                break
            else:
                money -= price
                print(Application())
                break
        else:
            pass
            
fn = input("Enter json filename : ")
data = read_json(fn)
shopping(data)
# print((data['customers']))
# print((data.get("customers"))[0])