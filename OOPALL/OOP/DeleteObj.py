class test:
    def __init__(self,name,age):
        self.name=name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)


ob1 = test('sajjadul',20)
ob1.display()
del ob1
