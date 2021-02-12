def gen(n):
    yield 1
    yield 34
    yield 32
    yield 23
    yield 12


g = gen(3)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))