for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a= l.index(max(l))
    b= l.index(min(l))
    print(a+1,b+1)