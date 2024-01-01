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

mod = 998244353

def solve():
    s = input()
    ans, cnt = 0, 1
    crr = 1
    k = 1
    for x in range(len(s)-1):
        if s[x]!=s[x+1]:
            k+=1
    for x in range(len(s)-1):
        if s[x]==s[x+1]:
            crr+=1
            ans+=1
        else:
            cnt *= max(1,crr)
            cnt %= mod
            crr = 1
    
    cnt *= max(1,crr)
    cnt %= mod
    for x in range(1,len(s)-k+1):
        cnt *= x
        cnt %= mod
    print(ans,cnt)




for _ in range(int(input())):
    solve()