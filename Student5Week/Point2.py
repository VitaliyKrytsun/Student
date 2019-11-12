class Point(object):
      
    def __init__ (self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

class Point2(Point):
    def print(self):
        super(Point, self)
    

class Point3(Point):
    def print(self):
        super(Point, self)

class Circle(Point):
    def print(self):
        super(Point, self)

p2 = Point(10, 20, 30, 40)
print("Точка Point2 з кординатами х = %s y = %s" % (p2.x, p2.y))

p3 = Point(10, 20, 30, 40)
print("Точка Point2 з кординатами х = %s y = %s z = %s" % (p3.x, p3.y, p3.z))

pc = Point(10, 20, 30, 40)
print("Коло з кординатами центра х = %s, y = %s і радіусом r = %s" % (pc.x, pc.y, pc.r))
