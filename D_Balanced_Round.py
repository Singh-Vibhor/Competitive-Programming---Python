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
    l = linput()
    l.sort()
    mx = 0
    crr = 1
    for x in range(1,n):
        if l[x]-l[x-1]<=k:
            crr+=1
        else:
            mx = max(mx,crr)
            crr = 1
    mx = max(mx,crr)
    print(n-mx)



for _ in range(int(input())):
    solve()