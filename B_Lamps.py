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



for _ in range(int(input())):
    n = int(input())
    d = defaultdict(list)
    ans = 0
    for x in range(n):
        a,b = linput()
        d[a].append(b)

    for x in d.keys():
        d[x].sort(reverse=True)
        if len(d[x])>=x:
            ans+=sum(d[x][:x])
        else:
            ans+=sum(d[x])
    
    print(ans)