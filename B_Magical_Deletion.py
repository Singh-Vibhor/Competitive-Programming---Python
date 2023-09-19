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
    s,k = input().split()
    k = int(k)
    n = len(s)
    brk = n-k
    for x in range(n-k):
        if s[x]>s[x+k]:
            brk = x
            break
    ans = s[:brk]+s[brk+k:]
    print(ans)



for _ in range(int(input())):
    solve()