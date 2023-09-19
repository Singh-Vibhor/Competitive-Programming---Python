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
    n,m,k = linput()
    x,y = linput()
    ax = x%2
    ay = y%2
    f = 1
    for z in range(k):
        x,y = linput()
        if (x%2==ax and y%2==ay) or (x%2!=ax and y%2!=ay):
            f = 0
    if f:
        print("YES")
    else:
        print("NO")



for _ in range(int(input())):
    solve()