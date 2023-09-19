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
    a,b = linput()
    a,b = min(a,b), max(a,b)
    diff = b-a
    if diff>a:
        print("NO")
        return
    if (a-diff)%3==0:
        print("YES")
    else:
        print("NO")



for _ in range(int(input())):
    solve()