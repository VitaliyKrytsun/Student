class Point2(object):
   
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def picters(self):
        return "Точка point2 з кординатами х = %s, y = %s" % (self.x, self.y)

p2 = Point2(20, 40)
print(p2.picters())


class Point3(object):
   
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def picters(self):
        return "Точка point2 з кординатами х = %s, y = %s, z = %s" % (self.x, self.y, self.z)

p3 = Point3(30, 60, 10)
print(p3.picters())



class Circle(object):
   
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        

    def picters(self):
        return "Коло з кординатами центра х = %s, y = %s і радіусом r = %s" % (self.x, self.y, self.r)

c = Circle(100, 100, 200)
print(c.picters())