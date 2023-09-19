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
    n,k = linput()
    a = linput()
    b = linput()
    l = [[x,y] for x,y in zip(a,b)]
    l.sort(key = lambda x:x[0])
    for x in l:
        if x[0]<=k:
            k+=x[1]
        else:
            break
    print(k)



for _ in range(int(input())):
    solve()