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
    n=int(input())
    l = linput()
    dp = [1]*(n+1)
    for x in range(1,n):
        
        for y in range(max(0,x-512),x):
            # print(l[x]^y,l[y]^x)
            if (l[y]^x < l[x]^y):
                dp[x] = max(dp[x], dp[y]+1)
    # print(dp)
    print(max(dp))




for _ in range(int(input())):
    solve()