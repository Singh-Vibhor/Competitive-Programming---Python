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
    n,k,x = linput()
    if k-1>(x) or k>n:
        print("-1")
        return
    sm = (k*(k-1))//2
    if x!=k:
        sm+=x*(n-k)
    else:
        sm+=(k-1)*(n-k)
    print(sm)



for _ in range(int(input())):
    solve()