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
    n,r = linput()
    if r>=n:
        print((n*(n-1))//2+1)
    else:
        print((r*(r+1))//2)



for _ in range(int(input())):
    solve()