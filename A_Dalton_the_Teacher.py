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
    cnt = 0
    for x in range(n):
        if l[x]==x+1:
            cnt+=1
    print((cnt+1)//2)



for _ in range(int(input())):
    solve()