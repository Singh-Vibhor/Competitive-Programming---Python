from collections import defaultdict
n,m = list(map(int,input().split()))
graph = defaultdict(list)

def dfs(start):
    visited[start] = 1
    for x in graph[start]:
        if not visited[x]:
            dfs(x)

for x in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)

visited = defaultdict(int)
ans = 0
for x in range(1,n+1):
    if visited[x]: continue
    dfs(x)
    ans+=1

print(ans)