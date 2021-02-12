import re


def r(pattern,st):
    rs = re.match(pattern,st)
    if rs:
        print(True)
    else:
        print(False)


r('M(d|st|s)\.?\s[A-Z]\w+','Mst. Sfsdjlfj$%')
r('[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|net.edu)','sba-p-@gm-ail.com')

r('htt(p|ps)//:+(www\.[a-zA-Z]|[a-zA-Z])+\.(com|edu|gov)','https//:appy.com')
r('https?//:(www\.)?(\w+)(\.\w+)','http//:hi.com')
r('(\-\+\.)?[0-9]+(\.)?[0-9]+','+2.90')