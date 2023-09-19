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
    a,b = linput()
    s = input()
    cnt = a//b
    c0 = 0
    f = 1
    ans = 0
    for x in s:
        if f and x=="1":
            ans+=a
            f = 0
            c0 = 0
            continue

        if x == "0":
            c0+=1
        elif x=="1":
            if c0<=cnt:
                ans+=c0*b
            else:
                ans+=a
            c0=0
        # print(ans,s)
    print(ans)



for _ in range(int(input())):
    solve()