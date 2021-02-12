def mcCarthy(n):
    if n > 100:
        return n - 10
    return mcCarthy(mcCarthy(n + 11))


while True:
    n = int(input())
    if (n == 0):
        break

    result = mcCarthy(n)
    print("f91({:d}) = {:d}".format(n, result))