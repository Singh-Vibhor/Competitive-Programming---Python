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



def solve():
    n,k = linput()
    l1 = linput()
    l2 = linput()
    dp = [[0,0] for x in range(n+1)]

    dp[0][0] = dp[0][1] = k
    ovans = k

    for x in range(n):
        dv = l2[x]
        dp[x+1][0] = dp[x][0]
        dp[x+1][1] = dp[x][1]
        if dv==1:
            clr1 = 0
            if dp[x][0]>=1900:
                clr1 = (-dp[x][0] + l1[x])/4
                clr1 = int(clr1)
                dp[x+1][0] = dp[x][0]+clr1

            if dp[x][1]>=1900:
                clr2 = (-dp[x][1] + l1[x])/4
                clr2 = int(clr2)
                # print(clr2)
                dp[x+1][1] = max(dp[x][1]+clr2, dp[x][0])
            
        
        else:
            clr1 = 0
            if dp[x][0]<=2100:
                clr1 = (-dp[x][0] + l1[x])/4
                clr1 = int(clr1)
                dp[x+1][0] = dp[x][0]+clr1


            if dp[x][1]<=2100:
                clr2 = (-dp[x][1] + l1[x])/4
                clr2 = int(clr2)
                # print(clr2)
                dp[x+1][1] = max(dp[x][1]+clr2, dp[x][0])

        
    print(min(k-dp[n][0], k-dp[n][1]))
    # print(dp)
        



for _ in range(1):
    solve()