class Point1(object):
   
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def picters(self):
        return "Точка point1 з кординатами х = %s, y = %s" % (self.x, self.y)

p1 = Point1(20, 40)
print(p1.picters())


class Point2(object):
   
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def picters(self):
        return "Точка point2 з кординатами х = %s, y = %s" % (self.x, self.y)

p2 = Point2(30, 60)
print(p2.picters())



class Circle(object):
   
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        

    def picters(self):
        return "Коло з кординатами центра х = %s, y = %s і радіусом r = %s" % (self.x, self.y, self.r)

c = Circle(100, 100, 200)
print(c.picters())