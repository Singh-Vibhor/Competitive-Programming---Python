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



def solve(s):
    d = {}
    for x in s:
        d[x] = d.get(x,0)+1
    ans = [s[0]]
    for x in s:
        # print(x,ans[-1],x>ans[-1])
        while len(ans) and x>=ans[-1] and d[ans[-1]]>0:
            ans.pop()
        ans.append(x)
        d[x]-=1
    return "".join(ans)



for _ in range(1):
    s = input()
    print(solve(s))