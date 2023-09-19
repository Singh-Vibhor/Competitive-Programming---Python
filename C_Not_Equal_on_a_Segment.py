from collections import defaultdict
from bisect import *
import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
l1 = list(map(int,input().split()))
dp = [-1]
for x in range(1,n):
    if l1[x]==l1[x-1]:
        dp.append(dp[x-1])
    else:
        dp.append(x-1)
# print(dp)
for x in range(m):
    l,r,x = list(map(int,input().split()))
    l-=1
    r-=1

    if l1[r]!=x:
        print(r+1)
        continue

    if dp[r]>=l:
        print(dp[r]+1)
        continue

    print(-1)
    