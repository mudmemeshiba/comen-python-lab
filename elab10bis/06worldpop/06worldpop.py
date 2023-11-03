import json

def read_file(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

def world_pop(data, inp):
    if inp == 1:
        print(len(data))

    if inp == 2:
        pop = 0
        for c in data:
            pop += int(c['population'])
        print(pop)
        
    if inp == 3:
        q1 = 0
        q2 = 0
        for c in data:
            if c['country'][0].lower() == 'c':
                q1 += 1
            if len(c['country']) > 5:
                q2 += 1
        print(q1)
        print(q2)

    if inp == 4:
        q1 = 0
        q2 = 0
        q3 = 0
        for c in data:
            if int(c['population']) > 500000000:
                q1 += 1
            if int(c['population']) >= 750000000:
                q2 += 1
            if int(c['population']) < 10000000:
                q3 += 1
        print(q1)
        print(q2)
        print(q3)

    if inp == 5:
        pop = 0
        world1 = 0
        world2 = 0
        for i in range(20):
            world1 += float(data[i]['World'])
        for i in range(49, 150):
            world2 += float(data[i]['World'])
        print(f"{(world1*100):.2f}")
        print(f"{(world2*100):.2f}")

fn = input("File Name: ")
inp = int(input("Input : "))
data = read_file(fn)
world_pop(data, inp)

# # worldpopulation.json
# ans = 70.40, 12,70
