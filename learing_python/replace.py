import string
str='sajjadul'
print(str.replace('a','b'))
print(str)

str=string.punctuation
print(str)

str=string.digits
print(str)

str=string.ascii_letters
print(str)
str=string.ascii_lowercase
print(str)

str=string.ascii_uppercase
print(str)

str=string.hexdigits
print(str)

str=string.printable
print(str)

str=string.whitespace
print(str)

titles="Hi Sajjadul Islam"
print(titles.istitle())

sp="hi sajjadul islma bappy"
lists=sp.split()
for i in lists:
    print(i)