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
    n = int(input())
    l = linput()
    # prf = [l[0]]
    # suf = [l[-1]]
    # for x in range(1,n):
    #     if l[x]<=prf[-1]:
    #         prf.append(l[x])
    #     else:
    #         prf.append(prf[-1])
    
    # for x in range(n-2,-1,-1):
    #     if l[x]<=suf[-1]:
    #         suf.append(l[x])
    #     else:
    #         suf.append(suf[-1])
    
    # # print(prf,suf)
    
    # for x in range(n):
    #     if prf[x]+suf[-x-1]<l[x]:
    #         print("NO")
    #         return
    # print("YES")
    s = 0
    for x in range(n-1):
        s+=max(0,l[x]-l[x+1])
    if s<=l[0]:
        print("YES")
        return
    print("NO")

for _ in range(int(input())):
    solve()