h = int(input("Enter horizontal shift size: "))
v = int(input("Enter vertical shift size: "))
image = []  #lists of strings
pixel = []  #single chars
imageList = [] #sublists of chars 
newList   = []

print("Enter image:")
while True:
    img = input("")
    if img != "-1":
        global lenImg
        lenImg = len(img)
    if img == "-1":
        break
    image.append(img)

# break strings in lists into list of chars
for i in range(len(image)):
    for px in image[i]:
        pixel.append(px)

# group into sublists
for i in range(len(image)):
    imageList.append(pixel[i*lenImg:(i+1)*lenImg])

# add zero to newList before moving image
# if we move first, it will fill the empty area
for i in range(len(image)):
    newList.append(["0"]*lenImg)

for i in range(len(image)-v): 
    for j in range(lenImg-h): 
        newList[i+v][j+h] = imageList[i][j]

print("After shift: ")
for i in range(len(image)):
    print("".join(newList[i]))

