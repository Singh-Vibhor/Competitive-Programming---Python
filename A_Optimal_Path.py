for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    ans=m*((n*(n+1))/2)+(m*(m-1))/2
    print(int(ans))