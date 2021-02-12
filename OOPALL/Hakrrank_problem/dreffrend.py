m = int(input())
ml = set(map(int, input().split()))
n = int(input())
nl = set(map(int, input().split()))
result = sorted(ml.difference(nl).union(nl.difference(ml)))

for i in result:
    print(i)