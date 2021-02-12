# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
l = set(map(int, input().split()))
input()
l2 = set(map(int, input().split()))
print(len(l.difference(l2)))