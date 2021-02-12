from collections import Counter
'''n=int(input())
l=list(map(int,input().split()))
n2=int(input())
sum = 0
for i in range(n2):
    c,d = map(int,input().split())

    if c in l:
        sum +=d
        l.remove(c)
        print(d)
print(sum)
'''
n = int(input())
l = Counter(map(int, input().split()))
n2 = int(input())
print(l)

sum = 0

for i in range(n2):
    a, b = map(int,input().split())
    if l[a]>0:
        sum +=b
        l[a] -=1
print(sum)