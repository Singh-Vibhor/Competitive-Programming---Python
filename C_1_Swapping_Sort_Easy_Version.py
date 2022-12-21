for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    le=[]
    lo=[]
    f=1
    for x in range(n):
        if l[x]%2==x%2:
            #print(x)
            f=0
            break
        if l[x]%2:
            lo.append(l[x])
        else:
            le.append(l[x])

    
    if f==0:
        print(-1)
    else:
        ans=0
        a1=len(lo)
        a2=len(le)
        for x in range(a1):
            for y in range(a1-x-1):
                if lo[y]>lo[y+1]:
                    temp=lo[y]
                    lo[y]=lo[y+1]
                    lo[y+1]=temp
                    ans+=1
                    #print(lo)
                    
        
        for x in range(a2):
            for y in range(a2-x-1):
                if le[y]>le[y+1]:
                    temp=le[y]
                    le[y]=le[y+1]
                    le[y+1]=temp
                    ans+=1
                    #print(le)
        print(ans)
        
                
        

