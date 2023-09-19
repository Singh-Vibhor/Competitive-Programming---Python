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
    xa,ya = linput()
    xb,yb = linput()
    xc,yc = linput()

    ans = 1
    if (xa-xb)*(xa-xc)>=0:
        ans += min(abs(xa-xb),abs(xa-xc))
    
    if (ya-yb)*(ya-yc)>=0:
        ans += min(abs(ya-yb), abs(ya-yc))
    
    print(ans)



for _ in range(int(input())):
    solve()