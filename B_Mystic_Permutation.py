for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if n==1:
        print(-1)
    else:
        b=list(range(1,n+1))
        for x in range(n-1):
            if a[x]!=b[x]:
                continue
            else:
                temp=b[x+1]
                b[x+1]=b[x]
                b[x]=temp
        if b[n-1]==a[n-1]:
            temp=b[n-2]
            b[n-2]=b[n-1]
            b[n-1]=temp

        print(" ".join(map(str,b)))     