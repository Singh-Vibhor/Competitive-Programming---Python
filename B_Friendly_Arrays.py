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
    n,m = linput()
    a = linput()
    b = linput()
    xor = 0
    for x in a:
        xor ^= x
    orr = 0
    for x in b:
        orr |= x
    
    a1,a2 = 0,0
    if n%2:
        a2 = xor
        for x in range(32):
            if xor&(2**x) or orr&(2**x):
                a1|=(2**x)
        
    else:
        a1 = xor
        for x in range(32):
            if not orr&(2**x) and xor&(2**x):
                a2 |= (2**x)
    
    print(a2,a1)
    




for _ in range(int(input())):
    solve()