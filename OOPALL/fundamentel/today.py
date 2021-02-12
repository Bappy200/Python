from datetime import date

d = date.today()

print(type(d))
print(d)

d2 = d.strftime('%A')
print(d2)
d2 = d.strftime('%d')
print(d2)
d2 = d.strftime('%D')
print(d2)
d2 = d.strftime('%x')
print(d2)
d2 = d.strftime('%X')
print(d2)
d2 = d.strftime('%w')
print(d2)
d2 = d.strftime('%I')
print(d2)
d2 = d.strftime('%p')
print(d2)