input()
l = set(map(int, input().split()))
input()
l2 = set(map(int, input().split()))

print(l.union(l2))
print(len(l.union(l2)))

