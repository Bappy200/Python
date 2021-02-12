for i in range(int(input())):
    aitem = int(input())
    a = set(map(int,input().split()))

    bitem = int(input())
    b = set(map(int,input().split()))

    re = a - b

    if re == set():
        print(re)
        print(True)
    else:
        print(re)
        print(False)