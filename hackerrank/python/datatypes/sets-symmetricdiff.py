# Enter your code here. Read input from STDIN. Print output to STDOUT
import sets

m = int(raw_input())
ml = set(map(int,raw_input().split()))

n = int(raw_input())
nl = set(map(int,raw_input().split()))

cool = list(ml.symmetric_difference(nl))
cool.sort()

for x in cool:
    print x