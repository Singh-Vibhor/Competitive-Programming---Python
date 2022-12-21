for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if n%2==1:
        print("Mike")
    else:
        mn=min(a)
        if a.index(mn)%2:
            print("Mike")
        else:
            print("Joe")
