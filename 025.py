from collections import defaultdict
from queue import Queue

n,m = list(map(int,input().split()))
graph = defaultdict(list)
for x in range(m):
    a, b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)

disst = [-1]*n
disen = [-1]*n

q = Queue()
visited = defaultdict(int)

crrmv = 0
start = 1
q.put(start)
f = 0
while not q.empty():
    a = range(q.qsize())
    #print(a, "a")
    for x in a:
        crr = q.get()
        #print(crr)
        disst[crr-1] = crrmv
        visited[crr] = 1
        for y in graph[crr]:
            if not visited[y]:
                visited[y] = 1
                q.put(y)
    crrmv+=1

q1 = Queue()
visited1 = defaultdict(int)

crrmv = 0
start = n
q1.put(start)
f = 0
while not q1.empty():
    a = range(q1.qsize())
    #print(a, "a")
    for x in a:
        crr = q1.get()
        #print(crr)
        disen[crr-1] = crrmv
        visited1[crr] = 1
        for y in graph[crr]:
            if not visited1[y]:
                visited1[y] = 1
                q1.put(y)
    crrmv+=1

print(disst, disen)
total = disst[n-1]
ans = set()
for x in range(n):
    for y in graph[x]:
        if disst[x-1]+disen[y-1]==total-1:
            ans.add(x)
            ans.add(y)

l = list(ans)
l.sort()
if total == -1:
    print(-1)
else:
    print(" ".join(map(str,ans)))
