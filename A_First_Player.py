# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))



l=[]
n=int(input())
for x in range(n):
    l.append(input().split())
    l[x][1] = int(l[x][1])

mn,ix = l[0][1],0
for x in range(n):
    if l[x][1]<mn:
        mn = l[x][1]
        ix = x
    
for x in range(n):
    print(l[(ix+x)%n][0])