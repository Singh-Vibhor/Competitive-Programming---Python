for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(b[0]-a[0],end=" ")
    for x in range(1,n):
        if a[x]>=b[x-1]:
            print(b[x]-a[x],end=" ")
        else:
            print(b[x]-b[x-1],end=" ")

    print()
