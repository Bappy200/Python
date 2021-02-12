
class Person:
    name = 'd'

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi {self.name} ! How are you? ")


person1 = Person("sajjadul")
person1.talk()


