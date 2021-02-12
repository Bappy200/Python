def rev_str(s):
    for i in range(len(s)-1,-1,-1):
        yield s[i]


for i in rev_str("sajjadul"):
    print(" ".join(i))
l = [1,2,3,4,5]
list_comperiction = [i**2 for i in l]
genatetor = (i**2 for i in l)

print(list_comperiction)
for i in genatetor:
    print(i, end=" ")

