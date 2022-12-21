from collections import defaultdict as dd
n,m=list(map(int,input().split()))
l=list(map(int,input().split()))
s=sum(l)
s=int
d=dd(int)
dis=0
cnt=0
for x in l:
    dis+=x
    d[dis]=1
    
