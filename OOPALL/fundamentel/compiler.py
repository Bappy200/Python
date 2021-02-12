def make_class(x):
    class new_class:
        def __init__(self,name):
            self.name = name

        def display(self):
            print(self.name,x)

    return new_class


cls = make_class(20)
ob = cls('sajjadul islam Bappy')
ob.display()