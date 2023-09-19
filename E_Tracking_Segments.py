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



def check(x,n, qr, seg):
    c = [0]*(n+1)
    for y in range(x):
        c[qr[y]] = 1
        # a = qr[y]
    for y in range(1,n+1):
        c[y]+=c[y-1]
    for y in seg:
        if c[y[1]] - c[y[0]-1] > (y[1]-y[0]+1)//2:
            # print(x,c)
            return True
    return False

def solve():
    qr = []
    seg = []
    n,m = linput()
    f = 1

    for x in range(m):
        seg.append(linput())
    seg.sort(key = lambda x:x[0])
    q = int(input())
    
    for x in range(q):
        qr.append(int(input()))
    
    start, end = 0, q
    while start<end-1:
        mid = (start+end)//2
        if check(mid, n, qr, seg):
            end = mid
            f = 0
        else:
            start = mid
    if not check(q,n, qr, seg):
        print(-1)
        return
    # if f:
    #     print(q)
    #     return
    print(end)


for _ in range(int(input())):
    solve()