class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def picters(self):
        return "Точка Point2 з кординатами х = %s, y = %s" % (self.x, self.y)

p2 = Point2D(20, 40)
print(p2.picters())

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def picters(self):
        return "Точка Point2 з кординатами х = %s, y = %s, z = %s" % (self.x, self.y, self.z)

p3 = Point3D(30, 60, 10)
print(p3.picters())

class Circle(Point2D):
    def __init__(self, x, y, r):
        
        super().__init__(x, y)
        self.r = r
        
    def picters(self):
        return "Коло з кординатами центра х = %s, y = %s і радіусом r = %s" % (self.x, self.y, self.r)

c = Circle(100, 100, 200)
print(c.picters())