'''
def display(data):
    def prints():
        print(data)
    prints()


d = display
d('rabby')
'''


def add(a,b):
    return a+b


def mult(a,b):
    return a*b


def opration(opra,a,b):
    return opra(a,b)


print(opration(add, 2, 2))
print(opration(mult, 4, 4))


