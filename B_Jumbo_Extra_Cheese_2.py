for _ in range(int(input())):
    n=int(input())
    mx=0
    sm=0
    for x in range(n):
        a,b=list(map(int,input().split()))
        mx=max(a,b,mx)
        sm+=(min(a,b))
    
    ans=2*mx+2*sm
    print(ans)
