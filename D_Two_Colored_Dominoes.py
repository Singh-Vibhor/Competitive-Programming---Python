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
    return print(''.join(map(str,l)))



def solve():
    n,m = linput()
    l = []
    for x in range(n):
        l.append([*input()])
    # for x in range(n):
    #     printl(l[x])
    mpl = defaultdict(int)
    mpu = defaultdict(int)
    fl = 0
    fu = 0
    for x in range(n):
        for y in range(m):
            # print(x,y,l[x][y])
            
            
            if l[x][y] == "U":
                if fu:
                    l[x][y] = "W"
                    l[x+1][y] = "B"
                    fu = 0
                else:
                    l[x][y] = "B"
                    l[x+1][y] = "W"
                    fu = 1
                mpu[x]+=1
    for y in range(m):
        for x in range(n):
            
            if l[x][y] == "L":
                if fl:
                    l[x][y] = "W"
                    l[x][y+1] = "B"
                    fl = 0
                else:
                    l[x][y] = "B"
                    l[x][y+1] = "W"
                    fl = 1
                mpl[y]+=1

            # if l[x][y] == "R":
            #     l[x][y] = "B"
            #     # mpl[y]+=1

            # if l[x][y] == "D":
            #     l[x][y] = "B"
                # mpl[y]+=1
    
    for x in mpl.values():
        if x%2:
            print("-1")
            return
    for x in mpu.values():
        if x%2:
            print("-1")
            return
    for x in range(n):
        printl(l[x])
            


for _ in range(int(input())):
    solve()