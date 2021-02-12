import math
a,b,c=map(int,input().split())
a=math.pow(a,2)
b=math.pow(b,2)
c=math.pow(c,2)
if(a==b+c):
    print("right")
elif(b==a+c):
    print("right")
elif(c==a+b):
    print("right")
else:
    print("wrong")
