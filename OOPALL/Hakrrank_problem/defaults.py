'''
n, m = map(int, input().split())
l = list()
for i in range(n):
    l.append(input())
for j in range(m):
    ch = input()
    count = 0
    index = 0
    for i in l:
        index += 1
        if ch == i:
            print(index, end=' ')
            count += 1
    if count == 0:
        print(-1)

    print()
'''
from collections import defaultdict

d = defaultdict(list)

n, m = map(int, input().split())

for i in range(1, n + 1):
    d[input()].append(str(i))

for i in range(m):
    print(' '.join(d[input()]) or -1)