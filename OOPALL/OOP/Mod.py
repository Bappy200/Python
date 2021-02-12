class _Privates:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


class Publics:
    def __init__(self, age):
        self.age = age

    def _prt(self):
        print('This is private function')

    def prt(self):
        print('This is not private function')


