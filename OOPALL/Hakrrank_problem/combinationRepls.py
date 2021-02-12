from itertools import combinations_with_replacement

s, n = input().split()
s = sorted(s)
result = combinations_with_replacement(s,int(n))
for x in result:
    print(''.join(x))