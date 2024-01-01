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



def solve():
    n = int(input())
    s = input()
    c1 = 0
    c2 = 0
    for x in range(n):
        if s[x] == 'B':
            c2+=1
        else:
            break


    for x in range(n-1,-1,-1):

        if s[x] == 'A':
            c1+=1
        else:
            break
        
    print(max(n-c1-c2-1,0))



for _ in range(int(input())):
    solve()