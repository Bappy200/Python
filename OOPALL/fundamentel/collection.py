from collections import Counter

a = Counter("sajajdul")
m = Counter('sajdul')

print(a)
a.update(m)
print(a)




b = Counter([1,2,3,4,5,1,4,5,8,9])
print(b)

c = Counter({1:'sajjadul',3:'bappy',2:'rabby'})
print(c)

d = Counter((1,2,3,4,5,6,2,3,4,6,7,8))
print(d)

e = Counter(name=4,age= 13)
print(e)
print(list(e.elements()))




