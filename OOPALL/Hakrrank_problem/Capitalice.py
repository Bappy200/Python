'''s=list(input())
s[0] = s[0].upper()
for i in range(len(s)):
    if s[i]==' ':
        s[i+1] = s[i+1].upper()

l = s.split()
print(l)
'''

def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s


if __name__ == '__main__':


    s = input()

    result = solve(s)
    print(result)


