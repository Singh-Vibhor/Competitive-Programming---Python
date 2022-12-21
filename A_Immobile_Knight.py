for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    if n==1 or m==1:
        print(1,1)
    elif n<4 or m<4:
        print(2,2)
    
    else:
        print(1,1)