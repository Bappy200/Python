class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return'sumation is {0:d}+{1:d}= {2:d}'.format(self.a, self.b, self.a+self.b)


ob = Test(2, 3)
print(str(ob))