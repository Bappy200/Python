from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    key = input()
    d[key] = d.get(key,0)+1

print(len(d),end=' ')
for i in d.items():
    print(i[1],end=' ')