import re
con = 'qwrtypsdfghjklzxcvbnm'
CON = 'QWRTYPSDFGHJKLZXCVBNM'
vowel = 'aeiou'
VOWEL = 'AEIOU'

r = re.findall('[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM][aeiouAEIOU]+[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]$','rabcdeefgyYhFjkIoomnpOeorteeeeet')
for x in r:
    print(x)