import re


def regu(pattern, textCase):
    result = re.match(pattern, textCase)

    if result:
        print('Search Successful')
    else:
        print('Search not Successful')


pattern = '^a...h$'
textCase = 'aefgh'
regu(pattern,textCase)

regu('[abc]','bdsfds') #start a, b, c any charecter

regu('mn*a','manfdkjmt')
regu('mn?a','maaan')

regu('[0-9]{2,4}','54345435435345435986ab')

regu('\Asa','sajjadul islam')
regu('\Aname','nams is ')

regu('\bfoo',' football ')

regu('\d', '99A')
regu('\d', 'python')

regu('\D','python')
regu('\D','23 python 12')

regu('a|b','cde')
regu('a|b','at')

regu('(a|b|c)xz','cxztd')
regu('(a|b|c)xz','bappyczx')

regu('\s','     sdf ')
regu('\s','hi im')

regu('\S','sldjf dksfj kdjfk')
regu('\S',' sldjf dksfj kdjfk')

regu('\w','_sdf56_')
regu('\w','&jccjv')

regu('\W','%6djfk')
regu('[^ 0-9a-zA-Z_]','%35')

regu('Python\Z','This is Python')



