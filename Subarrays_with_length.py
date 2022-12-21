from collections import defaultdict as dd
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d=dd(list)
    for x in range(n):
        d[a[x]].append(x+1)

    print(d)

    ans=0
    for x in d.keys():
        l=d[x]
        l1=len(l)
        for y in len(l1):
            if y==0:
                
