for _ in range(int(input())):
    x,k = list(map(int,input().split()))
    if x%k:
        print(1)
        print(x)
    else:
        print(2)
        print(x-1,1)