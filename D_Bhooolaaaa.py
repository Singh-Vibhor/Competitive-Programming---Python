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

add = [pow(2,x) for x in range(33)]


def solve():
    n,q = linput()
    l = linput()
    dp = [[0]*32 for x in range(n)]
    for x in range(n):
        if x>0:
            for y in range(32):
                dp[x][y] = dp[x-1][y]
        cr = 0
        y = l[x]
        while(y)>0:
            if y%2:
                dp[x][cr] += 1
            cr+=1
            y//=2
        
    #print(dp)

    for x in range(q):
        L,R = linput()
        x1 = 0
        x2 = 0
        x3 = 0
        ln = R-L+1
        for x in range(32):
            if L==1:

                if dp[R-1][x]>=((ln+1)//2):
                    x3+=add[x]

                if dp[R-1][x]>=1:
                    x1+=add[x]

                if dp[R-1][x]==ln:
                    x2+=add[x]
            else:
                if dp[R-1][x]-dp[L-2][x]>=((ln+1)//2):
                    x3+=add[x]

                if dp[R-1][x]-dp[L-2][x]==ln:
                    x2+=add[x]

                if dp[R-1][x]-dp[L-2][x]>0:
                    x1+=add[x]
        
        print(int(x1),int(x2),int(x3))



for _ in range(int(input())):
    solve()