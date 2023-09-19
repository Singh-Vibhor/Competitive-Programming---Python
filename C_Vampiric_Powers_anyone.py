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
    dp = [[0]*9 for x in range(n)]
    f = [0]*9
    for i,x in enumerate(l):
        cr = 0
        while x>0:
            dp[i][cr] = x%2
            if x%2:
                f[cr] = 1
            cr+=1
            x//=2
    
    ans = 0
    a1 = 0
    cr = 0
    for x in l[::-1]:
        cr^=x
        a1 = max(a1,cr)
    ptr = n-1
    acr = 0
    for x in range(7,-1,-1):
        if not f[i]:
            continue
        if acr& 2**x:
            continue
        if ptr==-1:
            break

        p1 = ptr
        if dp[ptr][x]==1:
            for y in range(7,x,-1):
                if dp[ptr][y]!=0:
                    f = 1
                    break
            if f==0:
                ans+=2**x
                ptr-=1
                acr = 0
                for x in range(len(l)-1,ptr,-1):
                    acr^=l[x]
                l.append(acr)
        p1-=1
        while p1>=0:
            if dp[p1][x]==1 and ((dp[ptr][y] - dp[p1][y] %2)==0 for y in range(7,x,-1)):
                ans+=2**x
                ptr = p1-1
                acr = 0
                for x in range(len(l)-1,ptr,-1):
                    acr^=l[x]
                l.append(acr)
                break
            else:
                p1-=1
    print(ans,a1)
    print(max(ans,a1))


        

        



for _ in range(int(input())):
    solve()