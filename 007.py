for _ in range(int(input())):
    n,b,x,y=list(map(int,input().split()))
    s=0
    num=0
    for i in range(n):
        if num+x>b:
            num=num-y
            s=s+num
        else:
            num=num+x
            s=s+num

    print(s)


    
    