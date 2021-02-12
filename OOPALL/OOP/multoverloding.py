class Dv:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '{0:d}*{1:d} = {2:d}'.format(self.a,self.b,self.a*self.b)

    def __mul__(self, other):
        a = self.a*other.a
        b = self.b*other.b
        return Dv(a,b)


ob = Dv(4, 4)
ob1 = Dv(2, 3)
print(ob.__mul__(ob1))
