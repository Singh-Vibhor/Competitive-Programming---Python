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

def convertBits(l):
    for x in range(len(l)):
        l[x] = [*bin(l[x]).replace('0b', '')]
        l[x] = ['0']*(32-len(l[x]))+l[x]
        l[x] = l[x][::-1]



def solve():
    n = int(input())
    l = linput()
    
    suf = [0]*n
    suf[n-1] = l[n-1]
    for x in range(n-2,-1,-1):
        suf[x] = suf[x+1] + l[x]
    
    ans = suf[0]
    for x in range(1,n):
        ans += max(0,suf[x])
    print(ans)
    



for _ in range(int(input())):
    solve()