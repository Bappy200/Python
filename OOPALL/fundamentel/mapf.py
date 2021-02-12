def func(n):
    return n**2


l = [1, 2, 3, 4, 5, 6, 7]
new_l = list(map(func,l))

print(new_l)
print(l)