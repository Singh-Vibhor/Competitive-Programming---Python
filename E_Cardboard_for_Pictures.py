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
    n,c = linput()
    l = linput()
    start = 0
    end = c
    while start<end:
        mid = (start+end)//2
        crr = 0
        for x in l:
            crr+= (x+mid)*(x+mid)
            if crr>c:
                break
        if crr==c:
            print(mid//2)
            return
        if crr<c:
            start = mid
        else:
            end = mid



for _ in range(int(input())):
    solve()