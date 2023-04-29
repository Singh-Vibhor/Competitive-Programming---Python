for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))

    cnt0 = l.count(0)
    cnt1 = l.count(1)
    if  cnt0+cnt1 != n:
        f=True
    else:
        f=False
    
    if cnt0<=(n+1)//2:
        print(0)
    elif f or cnt0 == n:
        print(1)
    else:
        print(2)