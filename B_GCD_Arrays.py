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
    l,r,k = linput()
    if l==1 and r==1:
        print("NO")
    elif l==r:
        print("YES")
    elif l%2 and k>=((r-l+2)//2):
        print("YES")
    elif l%2==0 and k>=((r-l+1)//2):
        print("YES")
    else:
        print("NO")



for _ in range(int(input())):
    solve()