import heapq
for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    l=list(map(int,input().split()))
    ans=0
    if l[m-1]>0 and n!=1:
        l[m-1]=-l[m-1]
        ans+=1
    
    l1=[]
    heapq.heapify(l1)


    sm=sum(l[:m])
    sm1=0

    for x in range(n):
        sm1+=l[x]
        #print(sm,sm1)
        if x!=m-1:
            heapq.heappush(l1,l[x])
        

        if sm1<sm:
            a=heapq.heappop(l1)
            sm1-=(2*a)
            ans+=1
    
    print(ans)

    
