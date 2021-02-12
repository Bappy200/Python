sup = set(map(int, input().split()))
result = []
for i in range(int(input())):
    sub = set(map(int,input().split()))
    if sup.issuperset(sub):
        result.append(True)
    else:
        result.append(False)
if False in result:
    print(False)
else:
    print(True)
