class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __mul__(self, other):
        if type(other) is not int:
            raise Exception('Invalid argument, must be int')

        self.name = self.name*other

    def __call__(self,x):
        if x % 2 == 0:
            print('Even')
        else:
            print('Odd')

    def __len__(self):
        return len(self.name)


p = Person('sajjadul')

print(p)
p(3)
p(4)
print(len(p))