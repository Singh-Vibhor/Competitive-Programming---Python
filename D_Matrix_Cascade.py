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
    ans = 0
    pos = [0]*(n+2)
    neg = [0]*(n+2)
    for x in range(n):
        prf = [pos[0]]
        for x in range(n):
            prf.append(prf[-1]+pos[x+1]-neg[x+1])
        # print(prf)
        s = input()
        for y in range(n):

            if (int(s[y])+prf[y])%2:
                ans+=1
                # print(x,y)
                pos[y]+=1
                neg[y+1]+=1
        # print(pos,neg)
        for x in range(1,n):
            pos[x-1]+=pos[x]
            pos[x] = 0
        # print(pos)
        for x in range(n,0,-1):
            neg[x+1] = neg[x]
            neg[x] = 0
        
    print(ans)

            



for _ in range(int(input())):
    solve()