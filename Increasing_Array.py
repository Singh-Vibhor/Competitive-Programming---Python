n=int(input())
l=list(map(int,input().split()))
prv = l[0]
ans = 0
for x in range(1,n):
    ans+=max(0,prv-l[x])
    prv = max(prv,l[x])
print(ans)