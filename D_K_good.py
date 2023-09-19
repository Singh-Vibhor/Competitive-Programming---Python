# IMSS
# I AM SAD SCAM

from collections import *
import math
import random
from sys import *
from heapq import *

input = stdin.readline 

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))


def solve():
    n = int(input())
    n1 = n
    a = 1
    while n>0 and n%2==0:
        n//=2
        a+=1
    if n==1:
        print(-1)
        return
    a = 2**a
    # print(a)
    if (a*(a+1))//2 <=n1:
        print(a)
    else:
        a = n1//(a//2)
        if (a*(a+1))//2 <= n1:
            print(a)
        else:
            print(-1)


for _ in range(int(input())):
    solve()