for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    l = list(map(int,input().split()))
    l2 = []
    l1 =[0]*m
    c1, c2 = 0, 0
    for x in l:
        if x==-1:
            c1+=1
        elif x==-2:
            c2+=1
        else:
            if x-1<m:
                l1[x-1]=1
                l2.append(x-1)
        
    for x in range(1,m):
        l1[x] += l1[x-1]
    
    mx = l1[m-1]
    
    ans=0
    ans = min(m,max(c1+l1[m-1],c2+l1[m-1]))
    
    for x in l2:
        left = min(x+1, c1+l1[x])
        right = min(m-x-1, c2+(l1[m-1]-l1[x]))
        #print(x+1, c1+l1[x])
        ans = max(ans,left+right)
    print(ans)
