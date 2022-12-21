from collections import defaultdict
for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    lh=list(map(int,input().split()))
    lp=list(map(int,input().split()))
    d=defaultdict(int)

    for x in range(n):
        d[lp[x]]=max(d[lp[x]],lh[x])
    
    lp.sort()

    crr=k
    x=0

    f=0
    while k>0:
        while d[lp[x]]<=crr:
            x+=1
            if x==n:
                f=1
                break
        #print(k,crr)
        #print(x)
        if x==n:
            break
        k-=lp[x]
        crr+=k
    
    if f:
        print("YES")
    else:
        print("NO")
