for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    ct=0
    for x in range(n):
        if l[x]==1:
            ct+=1
        else:
            break
    ans=(ct+1)//2+n-ct
    print(ans)