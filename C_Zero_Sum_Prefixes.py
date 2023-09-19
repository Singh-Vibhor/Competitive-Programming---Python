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
    n=int(input())
    l=linput()
    f = False
    freq = {}
    mxfr, crrsum, ans = 0, 0, 0
    for x in l:
        if x==0:
            if f:
                ans+=mxfr
            else:
                ans+=freq.get(0,0)
            f = True
            mxfr = 0
            freq.clear()
        
        crrsum+=x
        freq[crrsum] = freq.get(crrsum, 0)+1
        mxfr = max(mxfr,freq[crrsum])
    if f:
        ans+=mxfr
    else:
        ans+=freq.get(0,0)
    
    print(ans)
    

            



for _ in range(int(input())):
    solve()