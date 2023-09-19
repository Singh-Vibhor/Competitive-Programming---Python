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
    l1,r1 = linput()
    l2,r2 = linput()

    if l1+r1>l2+r2:
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    solve()