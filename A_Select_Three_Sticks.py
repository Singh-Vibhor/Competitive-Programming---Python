for _ in  range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=10**9
    l.sort()
    for x in range(n-2):
        sm=0
        sm+=l[x+1]-l[x]
        sm+=l[x+2]-l[x+1]

        ans=min(ans,sm)
    print(ans)
        