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
    n=int(input())
    l = linput()
    d = {}
    ans  = []
    for x in l:
        d[x] = d.get(x,0)+1
    ptr = 0
    mx = 0
    while d.get(mx,0):
        mx+=1
    
    cr = {}
    cur = 0

    used = 0
    while ptr<n:
        if mx == 0:
            ans += [0]*(n-used)
            break

        cr[l[ptr]] = cr.get(l[ptr],0)+1

        while cr.get(cur,0):
            cur+=1
        
        if cur==mx:
            # print(mx,ptr)
            ans.append(cur)
            mx = 0
            for x in cr.keys():
                d[x]-=cr[x]
                used+=cr[x]
            
            while d.get(mx,0):
                mx+=1
            # print(mx,"mx")
            cr = {}
            cur = 0
        ptr+=1
    print(len(ans))
    print(" ".join(map(str,ans)))




for _ in range(int(input())):
    solve()