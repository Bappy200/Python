from collections import deque

d = deque('sajjadul')
print(d.count('j'))
d.append('&')
print(d)

d.appendleft(5)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.remove('a')
print(d)

d.reverse()
print(d)

print(d.index('a'))

d.extend([1,2,3])
print(d)

d.rotate(-1)
print(d)