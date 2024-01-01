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
    n = int(input())
    l = linput()
    l.sort()
    mp = {}
    for x in l:
        mp[x] = mp.get(x,0)+1
    l1 = list(mp.keys())
    mx = 0
    for x in range(len(l1)):
        if l1[x]==mx:
            mx+=1
            continue
        break
    dp = [0]*(mx+1)
    for x in range(mx):
        dp[x] = mx*(mp[x]-1)

    for x in range(mx-1,-1,-1):
        for y in range(mx-1,x,-1):
            dp[x] = min(dp[x], dp[y]+y*(mp[x]))
    print(dp[0])

    
    



for _ in range(int(input())):
    solve()