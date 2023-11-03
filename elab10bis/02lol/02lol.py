import json

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

def caseZero(data, char):
    sortedChar = sorted(char)
    for key in data:
        for i in sortedChar:
            if data[key]['id'] == int(i):
                print(f"{key}\t---\t{data[key]['name']}\t---\t{data[key]['title']}")

def caseOne(data, char):
    sortedChar = sorted(char)
    for key in data:
        for i in sortedChar:
            if data[key]['name'][0] == i:
                print(f"{key}\t---\t{data[key]['name']}\t---\t{data[key]['title']}")

def caseTwo(data, char):
    sortedChar = sorted(char)
    for key in data:
        for i in sortedChar:
            if data[key]['title'][0] == i or data[key]['title'][4] == i:
                print(f"{key}\t---\t{data[key]['name']}\t---\t{data[key]['title']}")

filename = input("Filename : ")
case = int(input("Case : "))
char = input("Character : ").split(',')
data = read_json(filename)

if case == 0:
    caseZero(data, char)
elif case == 1:
    caseOne(data, char)
elif case == 2:
    caseTwo(data, char)

