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
    if n==1:
        print("NO")
        return
    ans = 0
    for x in l:
        if x==1:
            ans+=2
        else:
            ans+=1
    if ans>sum(l):
        print("NO")
        return
    
    print("YES")



for _ in range(int(input())):
    solve()