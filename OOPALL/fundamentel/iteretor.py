from itertools import product

a = [1,2]
b = [3,4]

pd = product(a,b,repeat=2)
c = len(list(pd))
print(c)