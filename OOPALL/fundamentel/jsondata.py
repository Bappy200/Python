import json
person = {'name':'Sajjadul islam bappy','age':20,'technology':'computers', 'hobby' : ['programming','problemsolving','development','design','Cricket','football']}
jsonPerson = json.dumps(person,indent=4)
#print(jsonPerson)
jo = json.loads(jsonPerson)
print(jo)

with open('persont.json', 'r') as file:
    jn = json.load(file)
    print(jn)

