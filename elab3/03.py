def fac(n,r):
    result = 1
    for x in range(n-r+1,n+1):
        result = x*result
    return result
# combi (5,2)
def combi(n,r):
    return int(fac(n,n-r)/fac(n-r,n-r)) 

ans = int((combi(4,3) + combi(7,3) + combi(3,3) + combi(7,3) + combi(10,3))/ 5)
print(ans)
# print(combi(4,3) + combi(7,3) + combi(3,3) + combi(7,3) + combi(10,3))/ 5
#  4,7,3,7 และ 10
# up fac(n,n-r)

# ใช้ combinatorics
# คำนวณ sum ของ combi แต่ละคน 5 คน แล้วหาร 5
