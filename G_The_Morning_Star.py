# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *

input = stdin.readline 
print = lambda s: stdout.write(str(s)+'\n')

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))



def solve():
    n = int(input())
    mpx = {}
    mpy = {}
    mpp = {}
    mpm = {}
    for i in range(n):
        x,y = linput()

        mpx[str(x)]=mpx.get(str(x),0)+1
        mpy[str(y)]=mpy.get(str(y),0)+1
        mpp[str(x+y)]=mpp.get(str(x+y),0)+1
        mpm[str(x-y)]=mpm.get(str(x-y),0)+1
    
    ans = 0
    for x in mpx.values():
        ans+=(x*(x-1))
    
    for x in mpy.values():
        ans+=(x*(x-1))

    for x in mpp.values():
        ans+=(x*(x-1))

    for x in mpm.values():
        ans+=(x*(x-1))
    print(ans)


for _ in range(int(input())):
    solve()