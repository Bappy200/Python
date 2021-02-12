K = int(input())
room = input().split()

set1 = set()
set2 = set()

for i in room:
    if i in set1:
        set2.add(i)
    else:
        set1.add(i)

re = list(set1.difference(set2))

print(re[0])