for _ in range(int(input())):
    n,q=list(map(int,input().split()))
    l=list(map(int,input().split()))
    ad=[0,l[0]]
    xr=[0,l[0]]
    for x in range(1,n):
        ad.append(l[x]+ad[x])
        xr.append(l[x]^xr[x])
    
    if q==1:
        L,R=list(map(int,input().split()))
        mx=0
        ansl=0
        ansr=n
        for x in range(R,L-1,-1):
            if ad[x]-ad[L-1]-xr[x]+xr[L-1]>=mx:
                mx=ad[x]-ad[L-1]-xr[x]+xr[L-1]
                a=xr[L-1]
                l1=L-1
                r1=x
                
                
#implement binary search for other indices