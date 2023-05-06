from collections import defaultdict
from queue import Queue
n,m = list(map(int,input().split()))
graph = defaultdict(list)
for x in range(m):
    a, b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)

start, target = list(map(int,input().split()))
q = Queue()
visited = defaultdict(int)

crrmv = 0
ans = 0

q.put(start)
f = 0
while not q.empty():
    a = range(q.qsize())
    #print(a, "a")
    for x in a:
        crr = q.get()
        #print(crr)
        if crr == target:
            ans = crrmv
            f = 1
            break
        visited[crr] = 1
        for y in graph[crr]:
            if not visited[y]:
                visited[y] = 1
                q.put(y)
    crrmv+=1

print(ans)
    
    
    