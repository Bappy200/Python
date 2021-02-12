'''from math import pow
from itertools import product
n, m = map(int,input().split())
l = [list(map(int,input().split())) for x in range(n)]
print(list(product(l)))
sq = [pow(max(x),2) for x in l]
print(sq)

result = sum(sq)%m
print('{:.0f}'.format(result))'''

from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split())) for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))
