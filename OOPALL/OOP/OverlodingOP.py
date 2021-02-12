class Num:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.x,' + ',self.y ,' = ',self.x+self.y

    def large_number(self):
        import math
        return math.sqrt(self.x+self.y)

    def __eq__(self, other):
        return self.large_number() == other.large_number()

    def __le__(self, other):
        return self.large_number() <= other.large_number()

    def __ge__(self, other):
        return self.large_number() >= other.large_number()


num1 = Num(9,4)
num2 = Num(6,3)
num3 = Num(6,7)

print(num1 == num2)
print(num1 <= num2)
print(num1 >= num3)
