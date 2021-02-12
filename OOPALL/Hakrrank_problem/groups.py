import re
r = re.search(r'(\w)\1+',input())
print(r.group(1) if r else -1)

