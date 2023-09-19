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
    n,d = linput()
    l = linput()
    mp = {}
    ans = 0
    for x in l:
        mp[x+d] = 1
        if x in mp:
            ans+=1
    print(ans)


for _ in range(1):
    solve()