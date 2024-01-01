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

def convertBits(l):
    for x in range(len(l)):
        l[x] = [*bin(l[x]).replace('0b', '')]
        l[x] = ['0']*(32-len(l[x]))+l[x]
        l[x] = l[x][::-1]



#remember binary search
#bitwise operator -> bitmask
def solve():
    n,q = linput()
    l = linput()

    # dp = [[0,x] for x in range(64)]
    # for x in range(64):
    #     for y in l:
    #         if not y&2**x:
    #             dp[x][0] += 2**x - (y&(2**x - 1))

    # print(dp)

    def check(mid, l):
        pass


    start = l[0]
    for x in l:
        start &= x

    end = 10**18+2
    while start + 1 < end:
        mid = (start + end) // 2
        if check(mid, l):
            start = mid
        else:
            end = mid



for _ in range(1):
    solve()