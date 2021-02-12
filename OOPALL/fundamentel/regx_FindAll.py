import re


def find(pattern,st):
    l = re.findall(pattern, st)
    print(l)


find('\d+','hi 67how are6, yo786u fin98e')
find('\D+','hello45 fin56e bappi5y 67')

find('\w+','hi %bap*py fine^ wh@th')
find('\W+','hi %bap*py fine^ wh@th')

find('[abc]+','hello af56inec thak acr')



