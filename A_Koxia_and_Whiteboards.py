for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    l=list(map(int,input().split()))
    l1=list(map(int,input().split()))
    for x in l1:
        a=min(l)
        s=l.index(a)
        l[s]=x
    print(sum(l))