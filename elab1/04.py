price = 12.55
output = f"Price in Euro: {price}"
print(output)

price = 12.54
output = f"Price in Swiss Franks: {price * 1.086}"
print(output)

price = 12.54
rate = 1.086
output = f"Price in Swiss Franks: {price * rate:10.2f}"
print(output)