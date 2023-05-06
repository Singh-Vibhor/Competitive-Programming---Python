from collections import defaultdict
n,p,k = list(map(int,input().split()))
l = list(map(int,input().split()))
d=defaultdict(int)
ans = 0
for x in l:
    x = (pow(x,4) - k*x)%p
    ans+=d[x]
    d[x]+=1
print(ans)