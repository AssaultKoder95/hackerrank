# Enter your code here. Read input from STDIN. Print output to STDOUT
a = list()
n = int(raw_input())
a = raw_input().split()
a = list(set(a))
a = list(map(int,a))
a.sort()
a.pop()
temp = a.pop()
print temp