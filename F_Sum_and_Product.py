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
    mp = {}
    for x in l:
        mp[str(x)] = mp.get(str(x),0)+1
    q = int(input())
    for x in range(q):
        x,y = linput()
        if (x*x)-(4*y)>=0:
            g = int(sqrt((x*x)-(4*y)))
            x1 = (x+g)//2
            x2 = (x-g)//2
            
            if x1*x2!=y:
                print(0, end = " ")
                continue
            if g==0:
                a = mp.get(str(x//2),0)
                # print()
                print((a)*(a-1)//2, end = " ")
                continue
            # print(x,g, mp)
            print(mp.get(str((x+g)//2),0)*mp.get(str((x-g)//2),0), end = " ")


        else:
            print(0, end = " ")

    print()



for _ in range(int(input())):
    solve()