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
    mp = {}
    for x in l:
        mp[x] = mp.get(x,0)+1
    ans = []
    crr = n-1
    mx = max(l)
    for x in sorted(list(mp.keys())):
        while mp[x]>0:
            mp[x]-=crr
            ans.append(x)
            crr-=1
    ans.append(mx)
    printl(ans)


for _ in range(int(input())):
    solve()