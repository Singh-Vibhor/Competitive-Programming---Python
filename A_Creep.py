for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    n1=n
    m1=m
    if n==0:
        print('1'*m)
    elif m==0:
        print('0'*n)
    else:
        s="10"
        s*=min(n,m)
        n-=min(n1,m1)
        m-=min(n1,m1)
        s+=('0'*n)
        s+=('1'*m)
        print(s)
    