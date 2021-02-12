from itertools import combinations
s, k = input().split()
s = sorted(s)
for i in range(1,int(k)+1):
    result = combinations(s,i)
    for x in result:
        print(''.join(x))