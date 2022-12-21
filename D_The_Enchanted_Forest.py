for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))


    if n==1:
        print(l[0]+k-1)

    elif k==n:
        ans=sum(l)
        ans+=int((n*(n-1))/2)
        print(ans)

    elif k<n:
        ans=0

        for x in range(k):
            ans+=l[x]
        sm=ans
        p1=0
        p2=k
        while(True):
            if p2==n-1:
                break
            sm=sm-l[p1]+l[p2]
            ans=max(sm,ans)
            p1+=1
            p2+=1
            
        
        ans+=int((k*(k-1))/2)
        print(ans)

    else:
        ans=sum(l)
        ans+=(k-1+k-n)*n//2
    
        
        print(ans)
