def getMatrix():
    m = []
    for i in range(3):
        row = input(f"Row {i+1} : ").split()
        m.append(row)

    for i in range(3):
        for j in range(3):
            m[i][j] = int(m[i][j])
    return m

def matrix_det(m):
    aei = m[0][0]*m[1][1]*m[2][2]
    bfg = m[0][1]*m[1][2]*m[2][0]
    cdh = m[0][2]*m[1][0]*m[2][1]
    ceg = m[0][2]*m[1][1]*m[2][0]
    bdi = m[0][1]*m[1][0]*m[2][2]
    ahf = m[0][0]*m[2][1]*m[1][2]
    detA = (aei+bfg+cdh)-(ceg+bdi+ahf)
    return detA
m = getMatrix()
print(matrix_det(m))