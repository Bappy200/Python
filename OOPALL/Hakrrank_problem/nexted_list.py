
test=int(input())
l=[[input(),float(input())] for i in range(test)]
sm= l[0][1]
bg=999999

for i in range(len(l)-1):
    if sm > l[i+1][1]:
        sm = l[i+1][1]
for i in range(len(l)-1):
    if bg > l[i+1][1] and sm != l[i+1][1]:
        bg = l[i+1][1]

new=[l[j][0] for j in range(len(l)) if bg == l[j][1]]

new.sort()
for i in new:
    print(i)

'''
import sys

N = int(sys.stdin.readline())
students = []
for _ in range(N):
    student = sys.stdin.readline().strip()
    grade = float(sys.stdin.readline())
    students.append([grade, student])

students.sort()

lowest = students[0][0]
# find first student with higher score
for s in students:
    if s[0] > lowest:
        sec_lowest = s[0]
        break

# print
for s in students:
    print(s)
    if s[0] == sec_lowest:
        print('r = ',s[1])
'''











