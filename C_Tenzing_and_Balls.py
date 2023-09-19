# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))



def solve():
    n=int(input())
    l=linput()
    dp = [0]*len(l)
    prv = dict()
    # f = -1
    for x in range(len(l)):
        dp[x] = max(dp[x],dp[x-1])
        if l[x] not in prv:
            prv[l[x]] = [x]
        else:
            for y in range(len(prv[l[x]])-1,-1,-1):
                dp[x] = max(dp[x], x-prv[l[x]][y]+1+dp[max(0,prv[l[x]][y]-1)])
                
            if dp[x]==dp[x-1]:
                # prv[l[x]].pop()
                prv[l[x]].append(x)
        # f = l[x]
        
    print(dp[len(l)-1])
    # print(dp)
# 1 2 5 2 3 3 6 7 5 5

for _ in range(int(input())):
    solve()