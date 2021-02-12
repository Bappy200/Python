class Pa:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "({0},{1})".format(self.a, self.b)

    def __add__(self, other):
        a = self.a+other.a
        b = self.b+other.b
        return Pa(a, b)


ob = Pa(2, 5)
ob1 = Pa(2, 2)


print(ob.__add__(ob1))
