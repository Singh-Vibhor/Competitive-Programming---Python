for _ in range(int(input())):
    n,k=list(map(int,input().split()))

    a=1
    b=n+1
    f=1
    while True:
        for x in range(k-1):
            b-=1
            print(b, end=" ")
            if b==a:
                f=0
                break
        if f==0:
            break
        print(a, end=" ")
        
        a+=1
        if a==b:
            f=0
        if f==0:
            break
    print()
