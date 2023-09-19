from collections import *
from sys import implementation
for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    l1=[0]
    for x in range(n-1):
        l1.append(l1[l[x]-1]+1)
    
    dpt=defaultdict(int)
    for x in l1:
        dpt[x]+=1
    
    
    for x in sorted(list(dpt.keys()),reverse=True):
        a=x
        break 
    
    # use binary search for searching the next level that has more nodes than the current ones and then continue 
    # the loop from there
    # start search from (a+1)/2
    # implement it later
      
    while(True):
        if dpt[a]>k or a==1:
            print(a)
            break
        else:   
            k-=dpt[a]
            if a%2:
                a1=int((a+1)/2)
                dpt[a1+1]+=dpt[a]
                dpt[a1]+=dpt[a]
                for y in range(a,a1,-1):
                    dpt[y]-=dpt[a]
            else:
                dpt[int(a/2)]+=(dpt[a]*2)
                for y in range(a,int(a/2),-1):
                    dpt[y]-=dpt[a]
            a-=1

    
    

