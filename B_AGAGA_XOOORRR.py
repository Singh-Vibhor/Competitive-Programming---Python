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
    xor = 0
    for x in l:
        xor^=x
    if xor==0:
        print("YES")
        return
    cnt = 0
    x1 = 0
    for x in l:
        x1^=x
        if x1==xor:
            cnt+=1
            x1 = 0

    if cnt>1:
        print("YES")
        return
    print("NO")



for _ in range(int(input())):
    solve()