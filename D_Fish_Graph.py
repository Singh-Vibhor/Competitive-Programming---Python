from collections import defaultdict

for _ in range(int(input())):
    graph = defaultdict(list)
    n,m = list(map(int,input().split()))
    for x in range(m):
        a, b = list(map(int,input().split()))
        graph[a].append(b)
        graph[b].append(a)
    cycles = []
    
    visited = defaultdict(int)
    
    def findCycles(crr, parent, par):
        if visited[crr]==2:
            return 
        
        if visited[crr]==1:
            
            pt = []
            cur = parent
            pt.append(cur)
            while cur != crr:
                cur = par[cur]
                pt.append(cur)
            cycles.append(pt)
            return
            
        par[crr] = parent
        visited[crr] = 1
        for x in graph[crr]:
            if x == par[crr]:
                continue
            findCycles(x, crr, par)
        
        visited[crr] = 2
            

    findCycles(1, 0, [0]*(n+1))
    visited = [0]*(n+1)
    findCycles(2, 0, [0]*(n+1))
    f = 1
    print(cycles)
    for x in cycles:
        if f==0: break
        d=defaultdict(int)
        for y in x:
            d[y]=1
        
        for y in x:
            ans = []
            for z in graph[y]:
                if d[z]==0:
                    ans.append([y,z])
                    if len(ans)==2:
                        for y in range(len(x)-1):
                            ans.append([x[y],x[y+1]])
                        ans.append([x[len(x)-1],x[0]])
                        f = 0
                        print("YES")
                        print(len(ans))
                        for x in ans:
                            print(" ".join(map(str,x)))
                        break
                        
        
    if f:
        print("NO")
        
