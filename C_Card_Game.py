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

def fact(n):
    return 1 if n == 0 else n * fact(n - 1)

def choose(n, k):
    return fact(n) // fact(k) // fact(n - k)

def calc(n):
    if n == 2:
        return [1, 0, 1]
    else:
        a = calc(n - 2)
        return [choose(n - 1, n // 2) + a[1], choose(n - 2, n // 2) + a[0], 1]




def solve():
    mod = 998244353
    n = int(input())
    a = calc(n)
    a = list(map(lambda x: x % mod, a))
    print(*a)



for _ in range(int(input())):
    solve()