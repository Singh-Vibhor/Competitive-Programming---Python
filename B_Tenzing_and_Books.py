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
    n,x = linput()
    a = linput()
    b = linput()
    c = linput()
    ans = 0
    for y in a:
        if x|y!=x:
            break
        ans|=y
    for y in b:
        if x|y!=x:
            break
        ans|=y
    for y in c:
        if x|y!=x:
            break
        ans|=y
    if ans==x:
        print("YES")
    else:
        print("NO")
    



for _ in range(int(input())):
    solve()