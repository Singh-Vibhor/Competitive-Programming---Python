import heapq

a = int(input())
b = list(map(int,input().split()))
mp = {}

crr = 1
l = []
f = [0]*len(b)
heapq.heapify(l)
ans = []
while crr<=a:
    for x in range(len(b)):
        if not f[x] and b[x][0]<=crr:
            heapq.heappush(l,(b[1],b,b[2]))
    if not len(l):
        ans.append(-1)
        crr+=1
        continue
    a = heapq.heappop(l)
    l1 = a[1]
    ans.append(b.index(l1))
    c = a[2]
    c -= 1
    if c>0:
        heapq.heappush(l,(l1[1],l1,c))
    crr+=1

if len(l):
    print([-1])
else:
    print(ans)
                
                                    
            
            
            