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

# class SegmentTree:
    
#     tree = []
#     n = 0
    
#     def __init__(self, arr) -> None:
#         self.n = len(arr)
#         self.tree = [0]*(4*self.n)
#         self.buildTree(1,0,self.n-1,arr)
    
#     def buildTree(self, node, l, r, arr):
#         if l>r : return
#         if l==r:
#             self.tree[node] = arr[l]
#             return
        
#         mid = (l+r)//2
#         self.buildTree(2*node, l, mid, arr)
#         self.buildTree(2*node+1, mid+1, r, arr)
#         self.tree[node] = min(self.tree[node*2], self.tree[node*2+1])

#     def getMin(self, l, r):
#         return self._getMin(l, r, 0, self.n-1, 1)

#     def _getMin(self, l, r, treel, treer, node):
#         if treel>treer: 
#             return float('inf')
#         if treel>=l and treer<=r:
#             return self.tree[node]
#         if treel>r or treer<l: return float('inf')
#         if treel==treer and treel>=l and treer<=r: 
#             return self.tree[node]
#         mid = (treel+treer)//2
#         return min(self._getMin(l, r, treel, mid, 2*node),self._getMin(l, r, mid+1, treer, 2*node+1))
    

class SegmentTree:

    def __init__(self, arr) -> None:
        n = len(arr) - 1

        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16

        n += 1

        self.arr_len = n

        tree = [0] * (n-1) + arr + [float('inf')] * (n - len(arr))

        for i in range(n-2, -1, -1):
            tree[i] = min(tree[i*2 + 1: i*2 + 3])

        self.tree = tree
    
    def getMin(self, l, r):
        l += self.arr_len - 1
        r += self.arr_len - 1

        mn = float('inf')

        while (l <= r):

            if ((l % 2) == 0):
                mn = min(mn, self.tree[l])

                l = (l + 1 - 1) // 2
            else:
                l = (l - 1) // 2

            if ((r % 2) == 1):
                mn = min(mn, self.tree[r])

                r = (r - 1 - 2) // 2
            else:
                r = (r - 2) // 2

        return mn




def solve():
    n,q = linput()
    l = linput()
    tree = SegmentTree(l)
    for x in range(q):
        l,r = linput()
        print(tree.getMin(l-1,r-1))



for _ in range(1):
    solve()