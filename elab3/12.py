def eat(S,P,n):
    Paun  = S // P
    Gane  = (S - (Paun*P)) // n
    dog   = S-((P*Paun)+(n*Gane))
    return (Paun, Gane, dog)

S = int(input("Input starting food (S): "))
P = int(input("Input Paun's eating rate (P): "))
n = int(input("Input Gane's eating rate (n): "))


print(f"Paun eats {eat(S,P,n)[0]} time(s)")
print(f"Gane eats {eat(S,P,n)[1]} time(s)")
print(f"Remaining {eat(S,P,n)[2]} for dog")

print(eat(S,P,n))
# print(eat(S,P,n[2,1,0] - eat(S,P,n)[1,1,1])) not subscriptable
list = list(eat(S,P,n))
print(list)
newlist = [1,2,3]
subtract = list[0] - newlist[0]
print(subtract)