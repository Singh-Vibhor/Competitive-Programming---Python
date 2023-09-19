# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *
from bisect import bisect_left

input = stdin.readline 

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))

def get(a,b):
    for y in range(len(a)):
        if a[y]!=b[y]:
            return y
    return len(a)


def solve():
    n,m = linput()
    l = []
    for x in range(n):
        l.append(linput())
    
    l1 = [[0]*m for x in range(n)]
    for x in range(n):
        for y in range(m):
            l1[x][l[x][y]-1] = y+1
    
    l1.sort()

    for x in range(n):
        c = bisect_left(l1,l[x])
        ans = 0
        if c!=n: ans = max(ans,get(l1[c],l[x]))
        if c<n-1: ans = max(ans,get(l1[c+1],l[x]))
        if c>0: ans = max(ans,get(l1[c-1],l[x]))
        print(ans, end = " ")
    print()




for _ in range(int(input())):
    solve()