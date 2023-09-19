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
    l = linput()
    l.sort()
    crr = 0
    for x in range(n):
        if crr>0:
            l[x] = -l[x]
            crr+=l[x]
        else:
            crr+=l[x]
    
    printl(l)




for _ in range(int(input())):
    solve()