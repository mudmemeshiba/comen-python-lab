from math import ceil
cA=0
cB=0
cC=0
cO=0
pA=0
pB=0
pC=0
pO=0
pS=0
dA=0
dB=0
dC=0
dO=0
def merchant():
    global cA,cB,cC,cO,pA,pB,pC,pO,pS,dA,dB,dC,dO
    cA=float(input("weight of cargo to A: "))
    cB=float(input("weight of cargo to B: "))
    cC=float(input("weight of cargo to C: "))
    cO=float(input("weight of cargo to O: "))
    pA=float(input("price of cargo to A: "))
    pB=float(input("price of cargo to B: "))
    pC=float(input("price of cargo to C: "))
    pO=float(input("price of cargo to O: "))
    pS=float(input("price of supply: "))
    dA=float(input("distance O to A: "))
    dB=float(input("distance A to B: "))
    dC=float(input("distance B to C: "))
    dO=float(input("distance C to O: "))
    return cA,cB,cC,cO,pA,pB,pC,pO,pS,dA,dB,dC,dO
def traverse(w):
    return 90/(3+w)+5
def Cday(d,v):
    return ceil((d/v)/24)
def dlsale(d,cT,cs,pc,ps):
    v=traverse(cT) #ok
    sell=cs*pc
    spend=Cday(d,v)*ps
    return sell-spend
def surplus():
    global cA,cB,cC,cO,pA,pB,pC,pO,pS,dA,dB,dC,dO
    cT=cA+cB+cC+cO
    sur=dlsale(dA,cT,cA,pA,pS)
    cT=cB+cC+cO
    sur=sur+dlsale(dB,cT,cB,pB,pS)
    cT=cC+cO
    sur=sur+dlsale(dC,cT,cC,pC,pS)
    cT=cO
    sur=sur+dlsale(dO,cT,cO,pO,pS)
    return sur
merchant()
splus=surplus()
print("result profit is %.3f"%splus)