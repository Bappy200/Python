from math import sqrt


class Polygon:
    def __init__(self,n):
        self.n = n
        self.sides = [0 for _ in range(n)]

    def inputSides(self):
        self.sides = [float(input('Enter side  {}  : '.format(i+1))) for i in range(self.n)]


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        s = (a+b+c)/2
        area = sqrt(s*(s-a)*(s-b)*(s-c))
        print('The Triangle area is {0:.2f}'.format(area))


ob = Triangle()
ob.inputSides()
ob.findArea()




