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

class SegmentTree():
    def __init__(self, array):
        n = len(array) - 1

        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16

        n += 1

        self.arr_len = n

        tree = [0] * (n-1) + array + [0] * (n - len(array))
        for i in range(n-2, -1, -1):
            tree[i] = max(tree[i*2 + 1: i*2 + 3])

        self.tree = tree

    def get_sum(self, l, r):
        l += self.arr_len - 1
        r += self.arr_len - 1

        sum = 0

        while (l <= r):

            if ((l % 2) == 0):
                sum += self.tree[l]

                l = (l + 1 - 1) // 2
            else:
                l = (l - 1) // 2

            if ((r % 2) == 1):
                sum += self.tree[r]

                r = (r - 1 - 2) // 2
            else:
                r = (r - 2) // 2

        return sum


    def get_index(self, l, r, val):
        l += self.arr_len - 1
        r = 2*self.arr_len - 1

        f = 1

        while (l <= r):

            if ((l % 2) == 0):

                if self.tree[l]>=val:
                    f = 0
                    break

                l = (l + 1 - 1) // 2
            else:
                l = (l - 1) // 2

            if ((r % 2) == 1):

                r = (r - 1 - 2) // 2
            else:
                r = (r - 2) // 2
        
        if f:
            return -1
        
        while l*2+2 < len(self.tree):
            if self.tree[l*2+1]>=val:
                l = l*2+1
            else:
                l = l*2+2
        self.tree[l]-=val
        ans = l-self.arr_len+1
        while l>0:
            l = (l-1)//2
            self.tree[l] = max(self.tree[l*2+1], self.tree[l*2+2])

        return ans




def solve():
    n,q = linput()
    l = linput()
    q = linput()
    tree = SegmentTree(l)
    ans = []
    for x in q:
        ans.append(tree.get_index(0,len(l),x)+1)
    printl(ans)



for _ in range(1):
    solve()