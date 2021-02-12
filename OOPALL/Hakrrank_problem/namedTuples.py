from collections import namedtuple

n = int(input())
items = input().split()
Student = namedtuple('student', items)

sum = 0
for i in range(n):
    items1, items2, items3, items4 = input().split()
    S = Student(items1, items2, items3, items4)
    sum += S.MARKS
print('{0:.2f}'.format(sum/n))


