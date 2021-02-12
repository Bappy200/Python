from itertools import combinations,combinations_with_replacement

a = [1,2,3,4]
cm = combinations(a, 3)
print(list(cm))

comrep = combinations_with_replacement(a,7)
print(list(comrep))