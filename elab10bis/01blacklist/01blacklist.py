import json

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

def blacklist(data, filename):
    jsonFile = read_json(filename)
    found = False
    for d in jsonFile: #each dict
        if data in d.values(): 
            print("Found in blacklist")
            print(f"name : {d['name']}")
            print(f"account number : {d['account number']}")
            print(f"ID number : {d['ID number']}")
            found = True
        if found == True:
            if filename == "test2.json":
                print(f"True Wallet : {d['True Wallet']}")
            if filename == "test3.json":
                print(f"True Wallet : {d['True Wallet']}")
                print(f"Telephone : {d['Telephone']}")
            break
    if found == False:
        print("Not found in blacklist")

filename = input("Filename : ")
data = input("Data : ")
blacklist(data, filename)