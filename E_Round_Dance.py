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


def noOfCycles(grp, n):
    rt = 0
    j=0
    visited = [0]*(n+1)
    for x in range(1,n+1):
        if not visited[x]:
            pt = x
            c=0
            ad = [0]*(n+1)
            ad[x] = 1
            visited[x] = 1
            x = grp[x]
            while True:
                ad[x] = 1
                visited[x] = 1
                x = grp[x]
                if ad[x] and x!=pt:
                    c=1
                if visited[x]:
                    break
                pt = grp[pt]
            rt+=c
            if c==0:
                j=1

    return rt+j


def solve():
    def dfs(grp, x):
        visited[x] = 1
        st = [x]
        while len(st):
            x = st.pop(0)
            visited[x] = 1
            for y in grp[x]:
                if not visited[y]:
                    visited[y] = 1
                    st.append(y)
        

    
    n=int(input())
    l=linput()
    grp = defaultdict(int)
    grp1 = defaultdict(list)
    for x,y in enumerate(l):
        grp[x+1] = y
        grp1[x+1].append(y)
        grp1[y].append(x+1)
    mn, mx = 1, 0
    visited = [0]*(n+1)
    for x in range(1,n+1):
        if not visited[x]:
            mx+=1
            dfs(grp1, x)
    
    mn = noOfCycles(grp, n)
    print(mn,mx)




for _ in range(int(input())):
    solve()