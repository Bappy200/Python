try:
    n=int(input('Enter the number :'))
    assert n%2==0
except:
    print('Not an even number!')
else:
    print(n/2)