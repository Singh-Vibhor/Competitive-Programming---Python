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
    l = []
    for x in range(3):
        l.append(input())
    winner = ""
    if l[0][0]==l[1][1]==l[2][2]:
        winner = l[0][0]
        if winner!=".":
            print(winner)
            return
    for x in range(3):
        if l[x][0]==l[x][1]==l[x][2]:
            winner = l[x][0]
            if winner!=".":
                print(winner)
                return
        if l[0][x]==l[1][x]==l[2][x]:
            winner = l[0][x]
            if winner!=".":
                print(winner)
                return
    if l[0][2]==l[1][1]==l[2][0]:
        winner = l[0][2]
        if winner!=".":
                print(winner)
                return
    if winner=="" or winner==".":
        print("DRAW")
    else:
        print(winner)
        
        



for _ in range(int(input())):
    solve()