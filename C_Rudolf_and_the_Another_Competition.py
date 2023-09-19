# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *
from functools import cmp_to_key


input = stdin.readline 

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))


def compare(a,b):
    if a[0]==b[0]:
        if a[1]>b[1]:
            return 1
        return -1
    if a[0]<b[0]:
        return 1
    return -1


def solve():
    n,m,h = linput()
    l = []
    start = [0,0]
    ans = 1
    for x in range(n):
        a = linput()
        a.sort()
        if a[0]>h:
            if x==0:
                start = [0,0]
            continue
        slv = 1
        f = 1
        penalty = a[0]
        for y in range(1,m):
            a[y]+=a[y-1]
            if a[y]>h:
                if x==0:
                    start = [slv,penalty]
                else:
                    if slv>start[0]:
                        ans+=1
                    elif slv==start[0] and penalty<start[1]:
                        ans+=1
                f = 0
                break
            penalty+=a[y]
            slv+=1   
        if f:
            if x==0:
                start = [slv,penalty]
            else:
                if slv>start[0]:
                    ans+=1
                elif slv==start[0] and penalty<start[1]:
                    ans+=1
        
    print(ans)
    
    





for _ in range(int(input())):
    solve()