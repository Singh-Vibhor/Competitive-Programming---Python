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



def solve(l):
    n = len(l)
    l1 = l.copy()
    l2 = []
    
    for x in l:
        l2.append(-x)
    heapify(l1)
    heapify(l2)

    mpmin = {}
    mpmax = {}

    mn = min(l1)
    mx = max(l1)
    if mn*2>=mx:
        return 0
    
    ptr = n-1
    while l1[0]*2<-l2[0]:
        mpmin[l[ptr]] = mpmin.get(l[ptr],0) + 1
        mpmax[l[ptr]] = mpmax.get(l[ptr],0) + 1

        while l1[0] in mpmin and mpmin[l1[0]]:
            mpmin[l1[0]] -= 1
            heappop(l1)

        while -l2[0] in mpmax and mpmax[-l2[0]]:
            mpmax[-l2[0]] -= 1
            heappop(l2)
        ptr -= 1
    
    ans = n-(ptr+1)

    print(ans)
    





for _ in range(1):
    l = linput()
    solve(l)