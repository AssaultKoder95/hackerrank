# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())
cool = list()
for x in xrange(t):
        
    il = raw_input().split()
    
    if il[0] == "insert":
        cool.insert(int(il[1]),int(il[2]))
    if il[0] == "print":
        print cool
    if il[0] == "pop":
        cool.pop()
    if il[0] == "reverse":
        cool.reverse()
    if il[0] == "sort":
        cool.sort()
    if il[0] == "append":
        cool.append(int(il[1]))
    if il[0] == "count":
        print cool.count(int(il[1]))
    if il[0] == "index":
        print cool.index(int(il[1]))
    if il[0] == "remove":
        cool.remove(int(il[1]))
    
