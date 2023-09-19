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
    neg = []
    for x in l:
        if x<0:
            neg.append(x)
    if len(neg):
        print(neg[0])
    else:
        print(max(l))



for _ in range(int(input())):
    solve()