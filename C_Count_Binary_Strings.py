m=998244353

n=int(input())
le=[-1]*(n+5)
lne=[-1]*(n+5)
f=1

for i in range(n):
    l=list(map(int,input().split()))
    if l[0]==2:
        f=0
    if f==1:
        for j in range(n-i):
            if l[j]==1:
                for x in range(i,i+j+1):
                    if le[x]!=-1:
                        le[x]=min(le[x],i)
                    else:
                        le[x]=i

                    if lne[x]>=i:
                        f=0
                        
            
            elif l[j]==2:
                if le[i+j]<=i and le[i+j]!=-1:
                    f=0
                    
                lne[i+j]=i

    
if f==0:
    print(0)
else:
    ans=2
    prv=-1
    for x in range(n):
        if lne[x]!=-1:
            if lne[x]<=prv:
                lne[x]=-1
            prv=max(prv,lne[x])
    for x in range(1,n):
        
        if le[x]!=le[x-1] or le[x]==-1:
            ans*=2
        
        
        if lne[x]!=-1:
            ans-=2

        ans=ans%m
    

    print(ans)

                
# whatever answer was wrong anyways
