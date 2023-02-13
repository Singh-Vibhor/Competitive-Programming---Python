for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    ans=0
    x=0
    if l[0]!=0:
        ans=1
    while x<n:
        if l[x]<=x:
            ans+=1
            while l[x]<=x:
                x+=1
                if x==n:
                    break
        else:
            x+=1

    print(ans)