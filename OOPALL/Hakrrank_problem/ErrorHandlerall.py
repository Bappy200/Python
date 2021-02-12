l = dir(locals()['__builtins__'])
c=0
for i in l:
    c += 1
    print(c, i)