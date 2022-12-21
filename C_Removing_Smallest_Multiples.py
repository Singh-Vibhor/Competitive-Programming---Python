from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    t=list(input())
    prv=0
    ans=0
    d=defaultdict(int)
    for x in range(1,n+1):
        for y in range(x,n+1,x):
            if t[y-1]=='1':
                break
            if d[y]==0:
                ans+=(x)
                d[y]=1
        
    print(ans)
# submit in pypy, python 3=tle



