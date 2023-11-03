def newton_cuberoot(x,y):
	if abs((x**3)-y) <= (10**-6):
		return x
	else:
		x = (y/(x**2)+(2*x))/3
	return newton_cuberoot(x,y)

def cuberoot(y):
	return newton_cuberoot(1.0, y)

y = cuberoot(8)
print(y)