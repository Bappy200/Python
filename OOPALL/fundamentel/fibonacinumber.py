def fibonaciNumber(n):
    a, b = 0, 1

    while a < n:
        yield a
        a, b = b, a+b


r = fibonaciNumber(30)
print(*list(r))

