for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(-1)
    else:
        if n%2:
            print(-1)
        else:
            print(n//2,n//2,0)  