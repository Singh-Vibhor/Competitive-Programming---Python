from collections import Counter as ct
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    mx=0
    for x in range(0,n-1):
        if l[x]==l[x+1]:
            continue
        mx=max((x+1)*(n-x-1),mx)
    if l[0]==l[n-1]:
        print(int(n/2))
    else:
        print(mx)
    
    
