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
    n,m = linput()
    a = linput()
    b = linput()
    if sum(a)>sum(b):
        print("Tsondu")
    elif sum(a)<sum(b):
        print("Tenzing")
    else:
        print("Draw")



for _ in range(int(input())):
    solve()