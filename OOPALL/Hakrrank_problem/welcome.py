n, m=map(int,input().split())
c='.|.'
l=n//2
t=m//2
for i in range(l):
    print((c*i).rjust(t-1,'-')+c+(c*i).ljust(t-1,'-'))
print('WELCOME'.center(m,'-'))

for i in range(l):
    f=i+1
    print((c*(l-f)).rjust(t-1,'-')+c+(c*(l-f)).ljust(t-1,'-'))