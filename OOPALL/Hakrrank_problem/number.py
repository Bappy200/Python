def test(s,command):
    ans=1
    for c in s:
        cmd='if  c.'+command+'(): ans= 0;'

    return ans
s=input()
v=['isalnum','isalpha','isdigit','islower','isupper'];
for e in v:
    print(test(s,e)==0)