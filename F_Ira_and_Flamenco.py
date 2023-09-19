# IMSS
# I AM SAD SCAM

from collections import *
import sys
input = sys.stdin.readline
from array import array
from heapq import *
MOD=10**9+7

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))

invs=[1]+[pow(i,-1,MOD) for i in range(1,200_001)]

 

def solve():
    nn, m = map(int, input().split())
    a = sorted(array('i', map(int, input().split())))
    ans, freq = 0, Counter(a)
    li = array('i', freq)
 
 
    n, r, c =len(li), 0, 1
 
    for l in range(n):
        while r < n and li[r] - li[l] < m:
            c *= freq[li[r]]
            c %= MOD
            r += 1
 
        if r - l != m:
            continue
 
        ans += c
        ans %= MOD
 
        c *= pow(freq[li[l]], -1, MOD)
        c %= MOD
 
    print(ans % MOD)



for _ in range(int(input())):
    solve()