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
    s1 = input()
    if s1[len(s1)-1] not in [*"123456789"]:
        s1 = s1[:len(s1)-1]
    s = [*s1]
    ct = -1
    if s[0]>="5":
        print("1"+("0"*len(s)))
        return
    for x in range(len(s1)-1,-1,-1):
        if x and s[x]>="5" and s[x-1]!="9":
            s[x-1] = str(int(s[x-1])+1)
            ct = x
    if s[0]>="5":
        print("1"+("0"*len(s)))
        return
    if ct==-1:
        print(s1)
    else:
        print("".join(s[:ct])+("0"*(len(s)-ct)))

    



for _ in range(int(input())):
    solve()