# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))



def solve():
    n,m = linput()
    l=linput()
    c = Counter(l)

    for x in range(1,m+1):
        a = c.get(x,0)
        if a>n-a:
            #print(a)
            print("NO")
            return
    print("YES")



for _ in range(1):
    solve()