d={1,2}
print(type(d))
dr={'name':'bappy','roll':915632}
print(dr['name'])

print(dr.get('name'))
try:
    print(dr['roll'])
except KeyError:
    print('error')


