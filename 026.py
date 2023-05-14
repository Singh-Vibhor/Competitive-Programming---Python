from collections import defaultdict

n, m, b = list(map(int,input().split()))
l = []
for x in range(n):
    l.append([*input()])

q = []
visited = defaultdict(int)

for x in range(n):
    for y in range(m):
        if l[x][y]=='S':
            st = (x,y,0)
            break
ans = -1
crrmv = 0
f = 0
q.append(st)
while len(q):
    a = range(len(q))
    for _ in a:
        crr = q.pop(0)
        visited[crr] = 1
        x = crr[0]
        y = crr[1]
        if l[x][y]=='G':
            f=1
            ans = crrmv
            break
        if x+1<n:
            if l[x+1][y]=='#' and crr[2]<b and not visited[(x+1,y,crr[2]+1)]:
                q.append((x+1,y,crr[2]+1))
                visited[(x+1,y,crr[2]+1)] = 1

            if l[x+1][y]!='#' and l[x+1][y]!='S' and not visited[(x+1,y,crr[2])]:    
                q.append((x+1,y,crr[2])) 
                visited[(x+1,y,crr[2])] = 1
            

        
        if x-1>=0:
            if l[x-1][y]=='#' and crr[2]<b and not visited[(x-1,y,crr[2]+1)]:
                q.append((x-1,y,crr[2]+1))
                visited [(x-1,y,crr[2]+1)] = 1
            if l[x-1][y]!='#' and l[x-1][y]!='S' and not visited[(x-1,y,crr[2])]:    
                q.append((x-1,y,crr[2])) 
                visited[(x-1,y,crr[2])] = 1



        if y+1<m:
            
            if l[x][y+1]=='#' and crr[2]<b and not visited[(x,y+1,crr[2]+1)]:
                q.append((x,y+1,crr[2]+1))
                visited[(x,y+1,crr[2]+1)] = 1
            if l[x][y+1]!='#' and l[x][y+1]!='S' and not visited[(x,y+1,crr[2])]:    
                q.append((x,y+1,crr[2])) 
                visited[(x,y+1,crr[2])] = 1




        if y-1>=0:
            if l[x][y-1]=='#' and crr[2]<b and not visited[(x,y-1,crr[2]+1)]:
                q.append((x,y-1,crr[2]+1))
                visited[(x,y-1,crr[2]+1)] = 1
            if l[x][y-1]!='#' and l[x][y-1]!='S' and not visited[(x,y-1,crr[2])]:    
                q.append((x,y-1,crr[2])) 
                visited[(x,y-1,crr[2])] = 1


    
    crrmv+=1
    if f: break
print(ans)