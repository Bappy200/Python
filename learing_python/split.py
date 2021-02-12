import string

str="hi bappy how are you ?"
sp=str.split()
for i in sp:
    print(i)
sp1=str.split("'")
a=''
for i in sp1:
    i.split("'")
    print(f'i ={i}\n ')
    a+=i
print(f'a= {a} \n')

str2="hi bappy how are you"
print(str2.capitalize())
print(str2.upper())
print(str2.lower())
print(str2.replace('bappy','sajjadul',1))
