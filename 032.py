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


# hit = 0
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.hit = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache.pop(key) 
            self.cache[key] = val
            return self.cache.get(key)
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys():
            if len(self.cache.keys()) == self.capacity:
                del self.cache[next(iter(self.cache))]
        else:
            self.cache.pop(key)
            self.hit+=1
        self.cache[key] = value
    
    def ck(self):
        # print(self.hit, self.capacity)
        return self.hit

def check(l,mid,k):
    mp = {}
    c = LRUCache(mid)
    for x in l:
        c.put(x,x)
    # a = c.ck
    # print(getattr(c,"hit"))
    if getattr(c,"hit")>=k:
        return True
    return False

def solve(l, k):
    st = 1
    en = len(l)+1
    while st<en-1:
        mid = (st+en)//2
        # print(mid,st,en,check(l,mid,k))
        if not check(l,mid,k):
            st = mid
        else:
            en = mid
    # print(st,en)
    if check(l,st,k):
        return st
    return en



for _ in range(1):
    l = linput()
    k = int(input())
    print(solve(l,k))