from itertools import groupby
s = input().strip()
r = [(len(list(y)),int(x)) for x,y in groupby(s)]
print(*r)

