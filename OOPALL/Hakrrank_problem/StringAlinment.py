c='*'
n=int(input())
for i in range(n):
    print((c*i).rjust(n,'-')+c+(c*i).ljust(n,'-'))

