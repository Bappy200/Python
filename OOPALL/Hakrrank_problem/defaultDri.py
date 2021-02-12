from collections import defaultdict
n, m= map(int, input().split())
d = defaultdict(list)
for i in range(n):
    s = input()
    d[i].append(s)


for i in range(m):
    s1 = input()

    for j in d:
        print(d.get(j))
        if d.get(j) == s1:
            print(j)
    print()


