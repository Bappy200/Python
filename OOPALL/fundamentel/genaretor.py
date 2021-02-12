def data_gen(n):
    i = 0
    while n>i:
        yield i
        i +=1

l = data_gen(10)
print(list(l))