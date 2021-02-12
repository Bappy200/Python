class Parrot:
    species = 'bird'

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def displayData(self):
        print('Name is : '+self.name)
        print('Age is : ',self.age)
        print('Species : '+self.species)
ob = Parrot('shlik',12)
ob.displayData()