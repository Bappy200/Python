class Car:
    car = []

    def __init__(self, name):
        self.name = name
        self.car.append(self)

    @classmethod
    def carlen(cls):
        return len(cls.car)

    def d(self):
        print(self.name)


    @staticmethod
    def bark(n):
        for i in range(n):
            print('Bark')

    def t(self,n):
        for i in range(n):
            print('b')


car1 = Car('BMW')
car2 = Car('Lambar kiny')

print(car2.carlen())
car1.bark(4)
car1.t(4)

