from itertools import groupby

a = [1, 2, 3, 4, 5]

gr = groupby(a, lambda x: x > 3)

for key, value in gr:
    print(key, list(value))