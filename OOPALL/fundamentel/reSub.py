import re


def sums(pattern,replace,strings):
    result = re.sub(pattern,replace,strings)
    print(result)


sums('\s','','hee ho e\n i am fine')
sums('\w+',' ','%^hello*(@fine')

