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
    s = input()
    n = int(input())

    st = []
    rmv = [0]*(len(s))
    rm = 1
    for x in range(len(s)):
        while len(st) and st[-1][0]>s[x]:
            rmv[st[-1][1]] = rm
            rm += 1
            st.pop()
        st.append([s[x],x])
    while len(st):
        rmv[st[-1][1]] = rm
        rm += 1
        st.pop()

    # print(rmv)
            

    crr = len(s)
    if s[-1] not in sorted("abcdefghijklmnopqrstuvwxyz"):
        crr-=1
    mov = 0
    while n>crr:
        n -= crr
        crr -= 1
        mov += 1
    
    crr = 0
    for x in range(len(s)):
        if rmv[x]>mov:
            crr+=1
        if crr==n:
            print(s[x], end = "")
            return




for _ in range(int(input())):
    solve()