from collections import defaultdict 
for _ in range(int(input())):
    n=int(input())
    d=defaultdict(int)
    l=[]
    for x in range(n):
        l1=list(map(int,input().split()))
        for y in l1[1:]:
            d[y]+=1
        l.append(l1[1:])
    ans="NO"
    for x in l:
        f=1
        for y in x:
            if d[y]==1:
                f=0
                break
        if f:
            ans="YES"

    print(ans)