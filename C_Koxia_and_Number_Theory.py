from collections import Counter as ct
from collections import defaultdict as dd
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    f=1
    c=ct(l)
    for x in c.values():
        if x>=2:
            f=0
            break
    
    for x in range(2,n+1):
        d=dd(int)
        for y in l:
            d[y%x]+=1
        #print(d)
        if len(d.keys())==x:
            f1=0
            for y in d.values():
                #print(y,f)
                if y==1:
                    f1=1
                    break
                #print(f1)
            if f and f1==0:
                f=0
        if f==0:
            break
    if f:
        print("YES")
    else:
        print("NO")
