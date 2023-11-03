def lvl(gold):
    if gold < 1000:
        lvl = 0
    elif 1000 <= gold < 2000:
        lvl = 1
    elif 2000 <= gold < 3000:
        lvl = 2
    elif 3000 <= gold < 4000:
        lvl = 3
    else:
        lvl = 4
    return int(lvl)

def mjoinir(lvl):
    if lvl == 0:
        print("Not enough gold.")
    else:
        print(" " + "o"*((lvl*3)+4))   #wt_b:  7 10 13 16
        for i in range((lvl*2)+1):     #hmid:  3  5  7  9
            print("o"*((lvl*3)+6))     #wmid:  9 12 15 18
        print(" " + "o"*((lvl*3)+4))
        for i in range(lvl+2):         #stick: 3  4  5  6           
            print(" "*(lvl+3) + "o"*lvl)
        for i in range(lvl):
            print(" "*(lvl+2) + "o"*(lvl+2))
        print(" "*(lvl+3) + "o"*lvl)
gold = float(input("Input Gold: "))
gold = int(gold)
lvl = lvl(gold)
mjoinir(int(lvl))