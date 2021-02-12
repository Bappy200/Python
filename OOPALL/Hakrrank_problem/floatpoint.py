import re


p = '[.+-]?\d?[.]?\d'
for i in range(int(input())):
    s = input()
    r = re.match(p,s)
    if r:
        print(True)
    else:
        print(False)


