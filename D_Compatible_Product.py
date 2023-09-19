n=int(input())
l=list(map(int,input().split()))
p = 1
sm = 0
mod = 998244353
for x in l:
    p*=x
    sm+=x
    p%=mod
# p*= sm
# p%=mod
print(p)