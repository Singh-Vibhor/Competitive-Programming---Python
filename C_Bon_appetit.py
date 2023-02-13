from collections import Counter
import heapq
for _ in range(int(input())):
    n, m = list(map(int,input().split()))
    g=list(map(int,input().split()))
    t=list(map(int,input().split()))
    c=Counter(g)
    t.sort(reverse=True)
    l=list(c.values())
    for x in range(len(l)):
        l[x]=-l[x]
    heapq.heapify(l)


    ans=0
    for x in t:
        c=heapq.heappop(l)
        if c>=0:
            break
        ans+=min(x,abs(c))
        heapq.heappush(l,c+x)
    print(ans)

