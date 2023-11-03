total_week = int(input("Estimated time : "))
week = total_week//8

l_phy, l_weight, l_fit = [], [], []
for i in range(week):
    print(f"Week{i+1}")
    phy = int(input("Physical therapy : "))
    l_phy.append(phy)
    weight = int(input("Weight training : "))
    l_weight.append(weight)
    fit = int(input("Fitness training : "))
    l_fit.append(fit)
recov = total_week*2.5
if sum(l_phy) < recov and sum(l_weight) < recov and sum(l_fit) < recov:
    print("Buzzy has not recovered in time.")
else:
    print("Buzzy has recovered in time.")


# result = all(sum(lst) < 80 for lst in [l_phy, l_weight, l_fit])