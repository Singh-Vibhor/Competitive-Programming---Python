import sys
input = sys.stdin.readline
from collections import defaultdict as dd
t=int(input())
while(t):
    t-=1
    n,m=list(map(int,input().split()))
    l=list(map(int,input().split()))
    ct=[0]*(n+1)
    l1=[]
    for x in range(1,m+1):
        a,b=list(map(int,input().split()))
        l1.append([a,b])
        ct[a]+=1
        ct[b]+=1
    ans=1000000001
    if m%2==0:
        ans=0
    else:
        
        for x in range(1,n+1):
            if ct[x]%2==1:
                ans=min(ans,l[x-1])
    
        
        for x in range(1,m+1):
            if ct[l1[x-1][0]]%2==0 and ct[l1[x-1][1]]%2==0:
                ans=min(ans,l[l1[x-1][0]-1]+l[l1[x-1][1]-1])
                
    sys.stdout.write(str(ans)+"\n")

    