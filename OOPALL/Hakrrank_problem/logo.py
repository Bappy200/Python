import time
'''
s = list(input())
t =time.time()
print(t)
st = []
cu = []

for i in s:
    if i not in st:
        st.append(i)
        cu.append(s.count(i))


for i in range(3):
    for j in range(i+1,len(st)):
        if cu[i] == cu[j]:
            if st[i] > st[j]:
                st[i],st[j] = st[j],st[i]
        elif cu[i] < cu[j]:
            st[j], st[i] = st[i], st[j]
            cu[i], cu[j] = cu[j], cu[i]
for i in range(3):
    print(st[i] , cu[i])
t1 =time.time()
print(t1)
print('{0:f}'.format(t-t1))

'''

a = input()
num = {}
t = time.time()
print(t)
for i in a:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1
m = [[i, num[i]] for i in num]
m.sort(key = lambda x:x[0])
m.sort(reverse = True, key = lambda x : x[1])
m = m[:3]
for i in m:
       print(i[0], i[1])
t1 = time.time()
print(t1)
print('{0:f}'.format(t-t1))






