# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *

input = stdin.readline 
mod = 998244353

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))

def convertBits(l):
    for x in range(len(l)):
        l[x] = [*bin(l[x]).replace('0b', '')]
        l[x] = ['0']*(32-len(l[x]))+l[x]
        l[x] = l[x][::-1]



def solve():
    n = int(input())
    l = linput()
    convertBits(l)
    # print(l)
    ans = 0
    for x in range(32):
        o = [0,0]
        e = [0,0]
        f = 0
        for y in range(n):
            # if l[y][x] == '1':
            #     f = 1-f
            # 1 0 1 0 1 0 1
            #     if f:
            #         o[0] += (y-o[1]+1)*(o[2])+1
            #         o[2] += 1
            #         o[1] = y
            #         ans += o[0]*(2**x)
            #         ans %= mod
            #     else:
            #         e[0] += (y-e[1]+1)*(e[2])+1
            #         e[2] += 1
            #         e[1] = y
            #         ans += e[0]*(2**x)
            #         ans %= mod

            if l[y][x] == '1':
                f = 1 - f
            
            if f:
                if l[y][x] == '1':
                    o[0] += o[1]
                    ans += o[0]
                o[1]+=1
                

            else:
                if l[y][x] == '1':
                    e[0] += e[1]
                    ans += e[0]
                e[1]+=1
            
    
    print(ans)
            





for _ in range(1):
    solve()