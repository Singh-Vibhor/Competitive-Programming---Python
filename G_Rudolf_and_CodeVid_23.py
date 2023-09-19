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

def decimalToBinary(n):
    return "{0:b}".format(int(n))



def solve():
    n,m = linput()
    graph = defaultdict(list)
    l1 = []
    for i in range(2**n):
        l1.append(decimalToBinary(i))
    l = input()
    for x in range(m):
        pass






for _ in range(int(input())):
    solve()