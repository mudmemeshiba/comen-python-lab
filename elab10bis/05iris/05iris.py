import json

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

def calAvg(typeData, data):
    t = typeData
    species = {}
    for i in range(len(data)):
        species_name = data[i]['species']
        if species_name not in species:
            species[species_name] = []
            print(species[species_name])
        species[species_name].append(data[i][t])
    for key, value in species.items():
        print(f"{key} = {sum(value)/len(value):.2f}")

fn = input("Filename : ")
typeData = input("type : ")
data = read_json(fn)
calAvg(typeData, data)


 