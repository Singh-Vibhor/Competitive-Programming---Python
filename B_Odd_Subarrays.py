for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    x=0
    while x<n-1:
        if a[x]>a[x+1]:
            ans+=1
            x+=1
        
        x+=1
    
    print(ans)
