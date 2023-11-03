count = 1
consec = 0
l_input  = []
l_consec = []
while True:
    # assigning var
    n = int(input(""))
    l_input.append(n)
    if count <= 2:
        np = n
        n0 = n
    # counting consec
    if count > 1 and n0 == n:
        consec += 1
    if count >= 1 and n0 != n and n0 == np:
        l_consec.append([consec, n0])
        consec = 1
    # storing var
    if count >= 3:
        np = n0 #pre-previous
        n0 = n  #previous
    count += 1
    if n == 0:
        break
max_consec = max(l_consec)
print(max_consec[0])
if max_consec[0] == 1:
    print(l_input[0])
else:
    print(max_consec[1])

    # counting consec
    # if count == 1:
    #     consec += 1
#----------------------------#
# checking var  
    # print(f"Count: {count}")
    # print(f"current input: {n}")
    # if count>=2:
    #     print(f"previous input: {n0}")
    # print(f"prepre input: {np}") 
#----------------------------#
    # checking var  
    # print(f"current input: {n}")
    # if count>=2:
    #     print(f"previous input: {n0}")
    # print(f"prepre input: {np}")
#----------------------------#
# if count > 1:   # checking var
#     print(f"previous input: {n0}")
#     print(f"current input: {n}")
#     print(f"consec: {consec}")
#     print(l_consec)