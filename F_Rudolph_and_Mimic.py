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
    n = int(input())
    l = linput()
    c = Counter(l)
    print("- 0")
    stdout.flush()
    l1 = linput()

    c1 = Counter(l1)
    for x in c1.keys():
        if c1[x]>c.get(x,0):
            l2 = [n-c1[x]]
            ptr = x
            for i,y in enumerate(l1):
                if x!=y:
                    l2.append(i+1)
            
            print("-"," ".join(map(str,l2)))
            stdout.flush()

            l = linput()

            for i,y in enumerate(l):
                if y!=ptr:
                    print("!", i+1)
                    print()
                    stdout.flush()
                    return
                
            print("- 0")
            stdout.flush()
            l = linput()

            for i,y in enumerate(l):
                if y!=ptr:
                    print("!", i+1)
                    print()
                    stdout.flush()
                    return
            
            print("- 0")
            stdout.flush()
            l = linput()

            for i,y in enumerate(l):
                if y!=ptr:
                    print("!", i+1)
                    print()
                    stdout.flush()
                    return
                    
    
    print("- 0")
    stdout.flush()
    l1 = linput()

    c1 = Counter(l1)
    for x in c1.keys():
        if c1[x]>c.get(x,0):
            l2 = [n-c1[x]]
            ptr = x
            for i,y in enumerate(l1):
                if x!=y:
                    l2.append(i+1)
            
            print("-"," ".join(map(str,l2)))
            stdout.flush()

            l = linput()

            for i,y in enumerate(l):
                if y!=ptr:
                    print("!", i+1)
                    print()
                    stdout.flush()
                    return
                
            print("- 0")
            stdout.flush()
            l = linput()

            for i,y in enumerate(l):
                if y!=ptr:
                    print("!", i+1)
                    print()
                    stdout.flush()
                    return
            
            print("- 0")
            stdout.flush()
            l = linput()

            for i,y in enumerate(l):
                if y!=ptr:
                    print("!", i+1)
                    print()
                    stdout.flush()
                    return
    
    print("- 0")
    stdout.flush()
    l1 = linput()

    c1 = Counter(l1)
    for x in c1.keys():
        if c1[x]>c.get(x,0):
            l2 = [n-c1[x]]
            ptr = x
            for i,y in enumerate(l1):
                if x!=y:
                    l2.append(i+1)
            
            print("-"," ".join(map(str,l2)))
            stdout.flush()

            l = linput()

            for i,y in enumerate(l):
                if y!=ptr:
                    print("!", i+1)
                    stdout.flush()
                    return
                
            print("- 0")
            stdout.flush()
            l = linput()

            for i,y in enumerate(l):
                if y!=ptr:
                    print("!", i+1)
                    stdout.flush()
                    return
            
            print("- 0")
            stdout.flush()
            l = linput()

            for i,y in enumerate(l):
                if y!=ptr:
                    print("!", i+1)
                    stdout.flush()
                    return



for _ in range(int(input())):
    solve()