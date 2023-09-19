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
    n = int(input())
    a1 = []
    a2 = []
    for x in range(n):
        m = int(input())
        l = linput()
        l.sort()
        a1.append(l[0])
        a2.append(l[1])
    x1 = min(a1)
    a2.sort()
    # print(a1,a2,x1)
    for x in a2[1:]:
        x1+=x
    print(x1)
    



for _ in range(int(input())):
    solve()