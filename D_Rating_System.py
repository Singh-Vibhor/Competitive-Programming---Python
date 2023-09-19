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
    n=int(input())
    l=linput()
    ans = 0
    ov = 0
    crr = 0
    mx = 0
    for x in l:
        crr+=x
        ov+=x
        if crr>0:
            crr = 0
        if crr<mx:
            ans = ov-crr
            mx = crr

    print(ans)




for _ in range(int(input())):
    solve()