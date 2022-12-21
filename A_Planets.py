from collections import defaultdict
for _ in range(int(input())):
    n,c=list(map(int,input().split()))
    l=list(map(int,input().split()))
    d=defaultdict(int)
    for x in l:
        d[x]+=1
    
    ans=0
    for x in d.values():
        if x>c:
            ans+=c
        else:
            ans+=x
    print(ans)