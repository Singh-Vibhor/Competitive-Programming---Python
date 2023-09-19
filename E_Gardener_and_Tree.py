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
    _ = input()
    n,k = linput()
    if n==1 and k>=1:
        print(0)
        return
    grp = [[] for x in range(n)]
    inco = [0]*(n)
    for x in range(n-1):
        a,b = linput()
        a-=1
        b-=1
        inco[a]+=1
        inco[b]+=1
        grp[a].append(b)
        grp[b].append(a)
    
    ans = [0]*n
    qu = []
    for x in range(n):
        if inco[x]==1:
            qu.append(x)
            inco[x] = 0
            ans[x]=1
    

    while len(qu):
        qu1 = []
        for a in qu:
            for x in grp[a]:
                if inco[x]!=1:
                    inco[x]-=1
                    if inco[x]==1:
                        qu1.append(x)
                        ans[x] = ans[a]+1
        qu = qu1
        
    
    ans1 = 0
    for x in range(n):
        if ans[x]>k:
            ans1+=1
    print(ans1)
    




for _ in range(int(input())):
    solve()