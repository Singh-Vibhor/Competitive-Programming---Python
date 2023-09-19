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
    ans = ""
    for x in range(8):
        s = input()
        for y in range(8):
            if s[y]!=".":
                ans+=s[y]
    print(ans)



for _ in range(int(input())):
    solve()