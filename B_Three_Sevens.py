from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    d = defaultdict(int)
    l=[]
    for x in range(n):
        m=int(input())
        m=list(map(int,input().split()))
        for y in m:
            d[y] = x
        l.append(m)

    ans = []
    for x,y in enumerate(l):
        f=1
        for z in y:
            if d[z]==x:
                ans.append(z)
                f=0
                break
        if f:
            ans = -1
            break
    
    if ans == -1:
        print(ans)
    else:
        print(" ".join(map(str,ans)))
        
    
