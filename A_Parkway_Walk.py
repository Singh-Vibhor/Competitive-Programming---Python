for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    s=sum(a)
    if m>=s:
        print(0)
    else:
        print(s-m)
