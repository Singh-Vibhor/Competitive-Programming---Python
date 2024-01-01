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



def check(x, a, k, l):
    s = [0]*32
    for i in range(32):
        s[i] = int(a[x][i]) - int(a[l-1][i])
        
        if s[i]==(x-l+1):
            s[i] = 1
        else:
            s[i] = 0

    s = ''.join(map(str,s))
    s = s[::-1]
    s = int(s,2)

    if s>=k:
        return True
    return False



def solve():
    n = int(input())
    a = linput()
    q = int(input())
    
    l1=a.copy()

    for x in range(n):
        a[x] = "{0:b}".format(int(a[x]))
        a[x] = '0'*(32-len(a[x]))+a[x]
        a[x] =  list(map(int,[*a[x]]))
        a[x] = a[x][::-1]

    for x in range(1,n):
        for y in range(32):
            a[x][y] += a[x-1][y]
    
    a = [[0]*32]+a



    for x in range(q):
        l,k = linput()
        if k>l1[l-1]:
            print(-1, end = " ")
            continue
        
        start = l
        end = n+1
        while start<end-1:
            mid = (start+end)//2
            if check(mid, a, k, l):
                start = mid
            else:
                end = mid

        print(start, end = " ")
    print()
    






for _ in range(int(input())):
    solve()