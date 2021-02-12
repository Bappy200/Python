def add(n):
    return n+2


ad = lambda n: n + 2

isOdd = lambda n: True if n%2 == 0 else False

isBig = lambda a, b, c: a if a>b and a>c else b if b>a and b>c else c



print(isBig(7,9,9))

print(isOdd(3))
print(ad(5))
print(add(5))