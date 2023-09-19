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
    while n>1:
        print(n, end=" ")
        if n%2:
            n*=3
            n+=1
        else:
            n//=2
    print(1)



for _ in range(1):
    solve()