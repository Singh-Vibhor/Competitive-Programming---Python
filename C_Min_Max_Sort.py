from collections import defaultdict as dd
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d=dd(int)
    for x in range(n):
        d[l[x]]=x
    
    ans=n//2
    if n%2:
        c=(n+1)//2
        if d[c+1]>d[c] and d[c-1]<d[c]:
            prvl=d[c]
            prvr=d[c]
            c1=c+1
            c2=c-1
            #print(c,c1,n)
            while d[c1]>prvr and d[c2]<prvl and c1<n+1:
                #print("hi")
                ans-=1
                prvr=d[c1]
                prvl=d[c2]
                c1+=1
                c2-=1
            print(ans)
                
        else:
            print(ans)
    else:
        c2=n//2
        c1=c2+1
        prvr=d[c2]
        prvl=d[c1]
        while d[c1]>prvr and d[c2]<prvl and c1<n+1:
            ans-=1
            prvr=d[c1]
            prvl=d[c2]
            c1+=1
            c2-=1
        print(ans)

    