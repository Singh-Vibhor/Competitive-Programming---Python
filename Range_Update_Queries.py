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
        # for i in range(n-2, -1, -1):
        #     tree[i] = sum(tree[i*2 + 1: i*2 + 3])

        self.tree = tree

    def get_element(self, i):
        
        node = self.arr_len - 1 + i

        value = self.tree[node]

        while node > 0:
            node = (node - 1) // 2

            value += self.tree[node]
        return value

    def update(self, l, r, value):

        l += self.arr_len - 1
        r += self.arr_len - 1

        while (l <= r):

            if ((l % 2) == 0):
                self.tree[l] += value

                l = (l + 1 - 1) // 2
            else:
                l = (l - 1) // 2

            if ((r % 2) == 1):
                self.tree[r] += value

                r = (r - 1 - 2) // 2
            else:
                r = (r - 2) // 2








def solve():
    n,q = linput()
    a = linput()
    tree = SegmentTree(a)
    for x in range(q):
        query = linput()
        if query[0]==1:
            tree.update(query[1]-1, query[2]-1, query[3])
        else:
            print(tree.get_element(query[1]-1))



for _ in range(1):
    solve()