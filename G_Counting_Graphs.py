# IMSS
# I AM SAD SCAM

from collections import *
from sys import *
from heapq import *

input = stdin.readline 

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))

mod=998244353

def solve():
    n,S=map(int,input().split())
    l=[tuple(map(int,input().split()))for i in range(n-1)]
    l.sort(key=lambda x:x[2])

    dsu = [i for i in range(n)]
    rank = [1]*n
    def find(v):
        stack=[v]
        while dsu[v]!=v:
            stack.append(dsu[v])
            v=stack[-1]
        while stack:
            dsu[stack[-1]]=dsu[v]
            v=stack.pop()
        return dsu[v]

    
    ans = 1
    for x in l:
        u = x[0]-1
        v = x[1]-1
        if find(u)!=find(v):
            ans = ans*pow(S-x[2]+1, rank[dsu[v]]*rank[dsu[u]]-1, mod)
            ans%=mod
            rank[dsu[u]]+=rank[dsu[v]]
            rank[dsu[v]] = 0
            dsu[v] = dsu[u]
    print(ans)


    




for _ in range(int(input())):
    solve()