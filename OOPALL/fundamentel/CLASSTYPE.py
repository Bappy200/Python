class Test:
    def show(self):
        print('show d')
    pass


def fnc(self):
    self.name = 'rabby'


n =4
t =(1,2,3,4)
print(type(Test))
print(type(int))
print(type(n))
print(type(list))

print(type(tuple))
print(type(t))

print(type(fnc))

ts = type('sal',(Test,),{'c':'bappy','fn':fnc})
t = ts()
print(t.c)
t.show()
t.fn()
print(t.name)


