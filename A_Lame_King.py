for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    a=abs(a)
    b=abs(b)
    print(2 * min(a,b) + max(0, 2 * (max(a,b) - min(a,b))-1))