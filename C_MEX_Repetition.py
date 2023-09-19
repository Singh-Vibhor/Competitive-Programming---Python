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
    l = linput()
    k%=(n+1)
    # ans = [0]*n
    # for x in range(n+1):
    #     mp = defaultdict(int)
    #     for y in l:
    #         mp[y] = 1
        
    #     for x in range(n):
    #         mx = 0
    #         while mp[mx]:
    #             mx+=1
    #         mp[l[x]] = 0
    #         mp[mx]+=1
    #         l[x] = mx
    #     printl(l)
    missing = ((n)*(n+1)//2)-sum(l)
    # l+=[missing]
    # l+=l
    # l = l+[missing]+l
    # printl(l[k:n+k])
    l+=[missing]
    ans = [0]*n
    for x in range(-k,n-k):
        ans[(x+k)] = l[x%(n+1)]
    printl(ans)





for _ in range(int(input())):
    solve()