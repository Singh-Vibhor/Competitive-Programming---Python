# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(''.join(map(str,l)))



def solve():
    s=input()
    ans = [""]*len(s)
    for y in range(len(s)):
        x = s[y]
        if x=="t":
            ans[y] = "c"
        
        elif x=="l":
            ans[y]="r"
        
        elif x=="f":
            ans[y]="k"
        
        else:
            ans[y] = x
    printl(ans)
            



for _ in range(int(input())):
    solve()