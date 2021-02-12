n = int(input())
l = set(map(int, input().split()))
p = int(input())
for i in range(p):
    a = input().split()
    if a[0] == 'pop':
        l.pop()
    elif a[0] == 'remove':
        l.remove(int(a[1]))
    elif a[0] == 'discard':
        l.discard(int(a[1]))


print(sum(l))

