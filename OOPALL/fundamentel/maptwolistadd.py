import operator
l = lambda x,y: x*y

a = [1,2,3,4]
b = [2,2,2,2]
r = map(l,a,b)
print(*list(r))

print(*list(map(operator.mul,a,b)))