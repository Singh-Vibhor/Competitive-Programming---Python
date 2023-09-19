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
    ans = max(l)
    for x in range(n-2,-1,-1):
        ans = max(ans,l[x])
        curr = l[x+1]
        used = 0
        for y in range(x,-1,-1):
            if l[y]>curr+1:
                break
            used += curr-l[y]+1
            if used <= k:
                curr+=1
                ans = max(ans,curr)
            else:
                break
        used = 0
        curr = l[x]
        if x and l[x+1]>=l[x-1]:
            curr = max(l[x-1],l[x])
            used+=max(l[x-1]-l[x],0)
            for y in range(x-1,-1,-1):
                if l[y]>curr+1:
                    break
                used += curr-l[y]+1
                if used <= k:
                    curr+=1
                    ans = max(ans,curr)
                else:
                    break
        ans = max(ans,curr)

    print(ans)



for _ in range(int(input())):
    solve()