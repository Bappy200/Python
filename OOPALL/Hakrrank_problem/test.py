def mcCarthy(n):
    if n > 100:
        return n - 10
    return mcCarthy(mcCarthy(n+11))

n=int(input())
if(n!=0):
    result=mcCarthy(n)
    print("f91({:d}) = {:d}".format(n,result))

if(1.45>1.46):
    print('a')
else:
    print('b')
N='pdf'
N.upper()
