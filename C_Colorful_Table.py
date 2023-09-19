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
    n,k = linput()
    l = linput()
    c = [0]*(n+1)
    l1 = sorted(l)
    m1 = {}
    m2 = {}
    for x in range(len(l)):
        if l[x] not in m2:
            m2[l[x]] = x
        m1[l[x]] = x

    for x in range(n-1,0,-1):
        if m2[l1[x-1]]>m2[l1[x]]:
            m2[l1[x-1]] = m2[l1[x]]
        
        if m1[l1[x-1]]<m1[l1[x]]:
            m1[l1[x-1]] = m1[l1[x]]
    # print(m1,m2)

    for x in range(1,k+1):
        if x in m1:
            print(2*(m1[x]-m2[x]+1), end = " ")
        else:
            print(0, end = " ")

    print()



    # for x in range(len(l)):
        # first index in array larger than curr value 
        # and last index in array larger than curr value






for _ in range(int(input())):
    solve()