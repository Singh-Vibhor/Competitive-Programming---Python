from collections import defaultdict as dd
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d=dd(list)
    for x in range(n):
        d[a[x]].append(x+1)

    ans=[0]*n
    flag=True
    for x in d.values():
        if len(x)==1:
            flag=False
            break
        for y in range(len(x)-1):
            ans[x[y]-1]=x[y+1]
        ans[x[len(x)-1]-1]=x[0]

    if flag:
        print(" ".join(list(map(str,ans))))
    else:
        print(-1)
