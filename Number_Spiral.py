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
    x,y = linput()
    if x>=y:
        if x%2:
            print((x-1)**2+y)
        else:
            print((x)**2-y+1)
    else:
        if y%2:
            print((y)**2-x+1)
        else:
            print((y-1)**2+x)



for _ in range(int(input())):
    solve()