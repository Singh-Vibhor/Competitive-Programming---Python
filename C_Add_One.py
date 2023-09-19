# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *

input = stdin.readline 

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))

# dp starting from 10 
# dp[i] represents number of digits reached after i operations have been applied to 10 
# 8 98
# 9 10 9
# 10 11 10
# dp[i] = dp[i-9] + dp[i-10]

mod = 10**9+7

dp = [2]*((2*(10**5))+1)
dp[9] = 3
for x in range(10,(2*(10**5))+1):
    dp[x] = (dp[x-9]+dp[x-10])%mod

def solve():
    n,m = linput()
    ans = 0
    while n>0:
        a = n%10
        if 10-a>m:
            ans+=1
            ans%=mod
        else:
            ans+=dp[m-(10-a)]
            ans%=mod

        n//=10
    print(ans)



for _ in range(int(input())):
    solve()