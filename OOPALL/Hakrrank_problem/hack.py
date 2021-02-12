n=int(input())
sum=0
if(n>0):
    for i in range(2,n+1,1):
        sum=sum+i;
else:
    i=-2
    while(i>=n):
        sum=i+sum;

        i=i-1;

print(sum)