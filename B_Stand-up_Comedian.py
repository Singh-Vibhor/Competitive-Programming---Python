for _ in range(int(input())):
    a1,a2,a3,a4 = list(map(int,input().split()))
    mx=a1+a2+a3+a4
    if a1==0:
        print(1)
    else:
        x=min(a2,a3)
        y=max(a2,a3)
        ans=a1
        ans+=2*x
        y-=x
        ans+=min(a1,y)
        if y>=a1:
            ans+=1
        a1-=y
        if a1>0:
            ans+=min(a1+1,a4)
        print(min(ans,mx))
