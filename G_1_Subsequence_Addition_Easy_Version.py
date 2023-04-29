for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    crr = 1
    l.sort()
    if l[0]!=1:
        print("NO")
    else:
        f=True
        for x in range(1,n):
            if l[x]<=crr:
                crr+=l[x]
            else:
                f=False
                print("NO")
                break
        if f:
            print("YES")