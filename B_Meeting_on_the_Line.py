from collections import defaultdict as dd
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l1=list(map(int,input().split()))
    
    x1=[l[x]+l1[x] for x in range(n)]
    x2=[l[x]-l1[x] for x in range(n)]

    print((max(x1)+min(x2))/2)
    
   