width2  = 0
length2 = 0
height2 = 0

def compute_rectangle_area(first_side, second_side):
    return first_side*second_side

def compute_surface_area(width,length,height):
    s1 = compute_rectangle_area(width, length)
    s2 = compute_rectangle_area(length, height)
    s3 = compute_rectangle_area(width, height)
    return 2*(s1+s2+s3)

def compute_volume(width,length,height): 
    return width*length*height

def output(width,length,height):
    return print(f"For [{width:.2f} x {length:.2f} x {height:.2f}] cuboid:"), print(f"Surface area = {compute_surface_area(width,length,height):.3f}"), print(f"Volume = {compute_volume(width,length,height):.3f}")

def twice(width,length,height):
    global width2, length2, height2
    width2  = width*2
    length2 = length*2
    height2 = height*2
    return width2, length2, height2

width  = float(input("Enter width: "))
length = float(input("Enter length: "))
height = float(input("Enter height: "))

output(width,length,height)
print('\n' + 'After doubling each side,')
twice(width,length,height)
output(width2,length2,height2)

# print(f"For [{width:.2f} x {length:.2f} x {height:.2f}] cuboid:")
# print(f"Surface area {compute_surface_area(width,length,height):.3f}")
# print(f"Volume = {compute_volume(width,length,height):.3f}")

# print('\n' + 'After doubling each side,')
# print(f"For [{(2*width):.2f} x {(2*length):.2f} x {(2*height):.2f}] cuboid:")
# print(f"Surface area {compute_surface_area(width,length,height):.3f}")
# print(f"Volume = {compute_volume(width,length,height):.3f}")
