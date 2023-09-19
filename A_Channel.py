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
    n,m,k = linput()
    s= input()
    crr = 0
    ans = 0
    ov = 0
    for x in s:
        if x=="+":
            crr+=1
            ov+=1
        else:
            crr-=1
        ans= max(ans,crr)
    
    if m+ans==n:
        print("YES")
    elif m+ov>=n:
        print("MAYBE")
    else:
        print("NO")



for _ in range(int(input())):
    solve()