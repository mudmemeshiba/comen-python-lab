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

a = Line(0,0,4,4)
# print(a.contains(0,-1))
# print(a.get_distance())
# print(a.get_y(2))
print(Line.contains(2,2))