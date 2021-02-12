import re

def searchs(pattern,strings):
    result = re.search(pattern,strings)
    print(result.group())
    print(result.start())
    print(result.span())
    print(result.end())



searchs('\w+','%^fdk 67^&df')