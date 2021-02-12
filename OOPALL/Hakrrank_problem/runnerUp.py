'''
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))

    arr.sort()
    bg=arr[n-1]
    ru=arr[0]


    for i in arr:
        if bg > i and ru < i:
            ru=i

    print(ru)




if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))

    big = arr[0]
    ru = arr[1]
    for i in arr:
        if big < i:
            ru = big
            big = i
        else:
            if ru < i and big != i:
               ru = i

    print(ru)

    def max(l):
        return sorted(set(l))[-2]


test = int(input())
l = map(int,input().split())
c=sorted(l)

b=max(l)
print(b)
print(c)

'''
n = int(input())
arr=list(map(int,input().split()))
bg, ru = -6000, -6000
for i in arr:
        if bg < i:
            ru=bg
            bg=i

        elif bg != i and ru < i:
            ru=i
print(ru)







