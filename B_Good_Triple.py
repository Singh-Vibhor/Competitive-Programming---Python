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
    s = input()
    n = len(s)
    while s[n-1]!='0' and s[n-1]!='1':
        n-=1
    ans = 0
    a = [n] * (n + 1)
    ans = 0
    
    for i in range(n - 1, -1, -1):
        a[i] = a[i + 1]
        j = 1
        while i + j + j < a[i]:
            if s[i] == s[i + j] and s[i] == s[i + j + j]:
                a[i] = i + j + j
            j += 1
        ans += n - a[i]
    print(ans)



for _ in range(1):
    solve()