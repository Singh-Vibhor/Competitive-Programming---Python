from collections import defaultdict
def hcfnaive(a, b):
    if(b == 0):
        return abs(a)
    else:
        return hcfnaive(b, a % b)

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d=defaultdict(int)
    for x in range(n):
        d[l[x]]=x+1
        
    l1=list(d.keys())
    ans=-1
    for x in l1:
        for y in l1:
            if hcfnaive(max(x,y),min(x,y))==1:
                ans=max(ans,d[x]+d[y])
    
    print(ans)