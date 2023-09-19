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
    l = linput()
    l.sort()
    if l[1]+l[2]>=10:
        print("YES")
    else:
        print("NO")



for _ in range(int(input())):
    solve()