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

def convertBits(l):
    for x in range(len(l)):
        l[x] = [*bin(l[x]).replace('0b', '')]
        l[x] = ['0']*(32-len(l[x]))+l[x]
        l[x] = l[x][::-1]



#remember binary search
#bitwise operator -> bitmask
def solve():
    n = int(input())
    a = linput()
    b = linput()
    
    p1 = []
    p2 = []

    for x in range(n):
        p1.append((-a[x]-b[x],-b[x],x))
        p2.append((-b[x]-a[x],-a[x],x))
    
    heapify(p1)
    heapify(p2)
    
    # print(p1,p2)
    
    used = {}
    A = 0
    B = 0
    
    # most optimal can also mean to save your something so on every move I can check whether we want to take or save
    for x in range(n):
        if x%2==0:
            while p1[0][2] in used:
                heappop(p1)
            
            while p2[0][2] in used:
                heappop(p2)

            c1 = -p2[0][0]
            c2 = -p1[0][0]
            # print(p1[0],p2[0],A,B)
            if c1>c2:
                used[p2[0][2]] = 1
                A += a[p2[0][2]] - 1

            # elif c1==c2:
            #     if -p2[0][1]>-p1[0][1]:
            #         used[p2[0][2]] = 1
            #         A += a[p2[0][2]] - 1
            #     else:
            #         used[p1[0][2]] = 1
            #         A += a[p1[0][2]] - 1

            else:
                used[p1[0][2]] = 1
                A += a[p1[0][2]] - 1
        
        else:
            while p1[0][2] in used:
                heappop(p1)
            
            while p2[0][2] in used:
                heappop(p2)

            c1 = -p2[0][0] 
            c2 = -p1[0][0]
            # print(p1[0],p2[0],A,B)
            if c1>c2:
                used[p2[0][2]] = 1
                B += b[p2[0][2]] - 1

            # elif c1==c2:
            #     if -p2[0][1]>-p1[0][1]:
            #         used[p2[0][2]] = 1
            #         B+= b[p2[0][2]] - 1
            #     else:
            #         used[p1[0][2]] = 1
            #         B += b[p1[0][2]] - 1
            else:
                used[p1[0][2]] = 1
                B += b[p1[0][2]] - 1
        
    print(A-B)
    


for _ in range(int(input())):
    solve()