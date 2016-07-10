# Enter your code here. Read input from STDIN. Print output to STDOUT

t =  int(raw_input())
aDict = {}

for x in range(0,t):
    
    a,b,c,d = [ xa for xa in raw_input().split() ]
    b , c , d = float(b) , float(c) , float(d)
    aDict[a]=(b+c+d)/3
    
valcheck = raw_input()

print("%.2f" % aDict[valcheck])
