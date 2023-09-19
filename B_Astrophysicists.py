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
    n,k,g = linput()
    if n==2:
        print(0)
    else:
        ans = n*((g+1)//2-1)
        ans-=ans%g

        print(min(ans,k*g))




for _ in range(int(input())):
    solve()