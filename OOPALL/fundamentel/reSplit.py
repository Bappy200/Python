import re


def spilts(pattern,strings):
    result = re.split(pattern,strings)
    print(result)

spilts('\d+','hi45 ho89w are% you9r')
