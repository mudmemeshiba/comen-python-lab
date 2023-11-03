import json

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

def checkPrice(data, product):
    product_price = []
    for i in range(len(data)):
        if data[i]['Product type'] == product:
            product_price.append([int(data[i]['Cost']), data[i]['Brand']])
    return product_price

def comparePrice(product_price):
    min_price = None
    min_brand = None
    for price, brand in product_price:
        if min_price == None or price < min_price:
            min_price = price
            min_brand = brand
    print(f"{min_brand} : {min_price}")

filename = input("Filename : ")
product = input()
data = read_json(filename)
product_price = checkPrice(data, product)
comparePrice(product_price)