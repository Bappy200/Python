# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split())
s = input().split()
a = input().split()
b = input().split()

r = [(i in a) - (i in b) for i in s]
print(sum(r))

