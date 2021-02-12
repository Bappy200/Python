from collections import Counter

a = Counter(a=4, b=2, c=3, d=-1)
b = Counter(a=2,b=3,c=2,d=2)

print(a+b)
print(a-b)
print(b-a)
print(a & b)
print(b & a)
print(a | b)