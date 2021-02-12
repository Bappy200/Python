from  collections import OrderedDict
'''
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(OrderedDict(sorted(d.items(),key=lambda t:t[0])))
print(sorted(d.items(), key=lambda t: t[0]))
p = sorted(d.items(),key= lambda t:len(t[0]))
print(p)
print(d['pear'])

ord = OrderedDict()
ord = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(ord.get('pear'))
n = ord.get('pear')
su = int(input())

ord['pear'] = n+su

print(ord.get('pear'))
'''

d = OrderedDict()
for _ in range(int(input())):
    key,b,value = input().rpartition(' ')
    d[key] = d.get(key,0)+int(value)


for k,v in d.items():
    print(k,v)



