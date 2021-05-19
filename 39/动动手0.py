import math as m

class Point:
    def __init__(self,x1,y1):
        self.x1 = x1
        self.y1 = y1
    def getx(self):
        return self.x1
    def gety(self):
        return self.y1

class Line():
    def __init__(self,r1,r2):
        self.x = r1.getx() - r2.getx()
        self.y = r1.gety() - r2.gety()
        self.len = m.sqrt(self.x*self.x + self.y*self.y)

    def result(self):
        return self.len

r1 = Point(1,1)
r2 = Point(4,5)
line = Line(r1, r2)
print(line.result())


