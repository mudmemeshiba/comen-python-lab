def plus(total,value):
    return total+value
def minus(total,value):
    return total-value

menu = int(input("How many food you have : "))
l_menu = []
for i in range(menu):
    # append each food's amount and quality to l_menu 
    ip = input("")
    food = ip.split()
    l_menu.append(food) 
# convert str to int list
lint_menu = [[int(x) for x in food] for food in l_menu]
total_value = 0
for i in range(menu):
    if lint_menu[i][1] == 1:
        total_value = plus(total_value, lint_menu[i][0])
    elif lint_menu[i][1] == -1:
        total_value = minus(total_value, lint_menu[i][0])
print(total_value)

# str to int and multiply
# lint_menu = [int(x) * int(y) for x, y in l_menu]
# total = 0
# for i in range(lint_menu):
#     if lint_menu[i] >= 0:
#         total = minus(total, lint_menu[i])

