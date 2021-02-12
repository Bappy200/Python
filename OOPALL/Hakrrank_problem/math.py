import math
AB,BC=int(input()),int(input())
hype=math.hypot(AB,BC)
print(hype)
print(BC/hype)
print(math.acos(BC/hype))
print(round(math.degrees(0.7853981633974484)))
res=round(math.degrees(math.acos(BC/hype))) #to calculate required angle
degree=chr(176)                                #for DEGREE symbol
print(res,degree, sep='')
