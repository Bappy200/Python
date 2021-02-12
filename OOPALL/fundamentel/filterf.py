def isOdd(n):
    return n%2 != 0


l = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(filter(isOdd,l)))
