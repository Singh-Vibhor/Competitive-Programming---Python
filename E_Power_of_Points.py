# IMSS
# I AM SAD SCAM

from collections import *
from sys import *
from heapq import *
from bisect import bisect_left

input = stdin.readline 

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))



def solve():
    n = int(input())
    l = linput()
    a1 = sorted(l)
    prf = [0]*n
    suf = [0]*n
    for x in range(1,n):
        prf[x] = prf[x-1]+ ((a1[x]-a1[x-1])*x)
        suf[-x-1] = suf[-x] + ((a1[-x] - a1[-x-1])*(x))
    
    ans = []
    for x in l:
        y = bisect_left(a1, x)
        ans.append(prf[y]+suf[y]+n)
    printl(ans)
    



for _ in range(int(input())):
    solve()