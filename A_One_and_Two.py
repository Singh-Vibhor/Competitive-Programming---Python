for x in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    cnt = 0
    for x in l:
        if x==2:
            cnt+=1
    if cnt%2:
        print(-1)
    else:
        c1 = 0
        for x,y in enumerate(l):
            if y==2:
                c1+=1
            if c1==cnt//2:
                print(x+1)
                break
