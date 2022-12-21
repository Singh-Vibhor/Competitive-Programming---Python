for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a1=n
    for x in range(n):
        if a[x]!=1:
            a1=x
            break
    if a1==n:
        print("0")
    else:
        for x in range(n-1,0,-1):
            if a[x]!=1:
                a2=x
                break
        
        print(a2-a1+2)

    