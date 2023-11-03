class Line:
    def __init__(self, x1, y1, x2, y2):
        self.slope = (y2 - y1) / (x2 - x1)
        self.y_intercept = y1-(self.slope*x1)
        self.start_point = [x1, y1]
        self.end_point = [x2, y2]

    def contains(self, x, y):
        if (x >= min(self.start_point[0], self.end_point[0])) and (x <= max(self.start_point[0], self.end_point[0])):
            if (y == (self.slope*x) + self.y_intercept):
                return True
            else:
                return False
        else:
            return False
    
    def get_distance(self):
        return (((self.get_x2()-self.get_x1())**2) + ((self.get_y2()-self.get_y1())**2))**0.5
    
    def get_x1(self):
        return self.start_point[0]
    def get_y1(self):
        return self.start_point[1]
    def get_x2(self):
        return self.end_point[0]
    def get_y2(self):
        return self.end_point[1]
    
    def get_y(self, x):
        if (x >= min(self.start_point[0], self.end_point[0])) and (x <= max(self.start_point[0], self.end_point[0])):
            return (self.slope * x) + self.y_intercept
        else:
            return -999.999

class LineApp(Line):
    def __init__(self):
        x1 = int(input("Enter x1 : "))
        y1 = int(input("Enter y1 : "))
        x2 = int(input("Enter x2 : "))
        y2 = int(input("Enter y2 : "))
        line1 = Line(x1, y1, x2, y2)
        print(f"value of x1 on this line is {x1:.3f}")
        print(f"value of x2 on this line is {x2:.3f}")
        print(f"value of y1 on this line is {y1:.3f}")
        print(f"value of y2 on this line is {y2:.3f}")
        print("==========")
        print("Check x and y are on this line ?")
        x = int(input("Enter x : "))
        y = int(input("Enter y : "))
        if line1.contains(x, y) == True:
            print(f"x = {x:.3f} and y = {y:.3f} are on this line")
        else:
            print(f"x = {x:.3f} and y = {y:.3f} are not on this line")
        print(f"Distance between startPoint and endPoint is {line1.get_distance():.3f}")
        print("==========")
        print("Find value of y that gives( x , y ) on this line")
        x = int(input("Enter x : "))
        print(f"value of y is {line1.get_y(x):.3f}")
        if line1.get_y(x) == -999.999:
            print(f"( x , y ) = ( {x:.3f} , {line1.get_y(x):.3f} ) is not on this line")
        else:
            print(f"( x , y ) = ( {x:.3f} , {line1.get_y(x):.3f} ) on this line")

LineApp()