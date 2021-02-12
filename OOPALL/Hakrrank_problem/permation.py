from itertools import permutations
s, n=input().split()
l=list(permutations(sorted(s),int(n)))

for i in l:
    print(''.join(i))
    print(i)
