from collections import defaultdict
from queue import Queue
n,m = list(map(int,input().split()))
l = []
for x in range(n):
    l.append([*input()])

for x in range(n):
    for y in range(m):
        if l[x][y]=='A':
            start = (x,y)
            break

ans = -1

q = []

crrmv = 0

q.append(start)
f = 0
while len(q):
    a = range(len(q))
    for _ in a:
        crr = q.pop(0)
        #print(crr, crrmv)
        x = crr[0]
        y = crr[1]
        if l[x][y] == 'B':
            ans = crrmv
            f = 1
            break
        l[x][y] = '#'
        if x+1<n  and l[x+1][y]!='#':
            q.append((x+1,y))  
            if l[x+1][y]!='B':
                l[x+1][y]='#'
        
        if x-1>=0 and l[x-1][y]!='#':
            q.append((x-1,y))  
            if l[x-1][y]!='B':
                l[x-1][y] = '#'

        if y+1<m and l[x][y+1]!='#':
            q.append((x,y+1))  
            if l[x][y+1]!='B':    
                l[x][y+1] = '#'

        if y-1>=0 and l[x][y-1]!='#':
            q.append((x,y-1)) 
            if l[x][y-1]!='B':
                l[x][y-1] = '#'
    if f: break
        
    crrmv+=1
print(ans)