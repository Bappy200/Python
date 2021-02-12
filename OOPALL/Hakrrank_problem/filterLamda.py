l=[1,2,3,4,5,6,7]
new_l = list(filter(lambda x: x%2 == 0,l))
print(new_l)
mp=list(map(lambda x: x % 2 == 0, l))
print(mp)
