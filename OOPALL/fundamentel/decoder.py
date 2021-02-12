'''def result(fnu):
    def inner():
        print('start')
        fnu()
        print('end')
    return inner

@result
def data():
    print('Hi how are your')

data()
'''


def start_decoder(fnc):
    def inner(x):
        print('start')
        re = fnc(x)
        print('end')
        return re
    return inner


@start_decoder
def div(x):
    print(x+2)

div(5)
