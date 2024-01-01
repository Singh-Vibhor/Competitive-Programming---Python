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
            tree[i] = sum(tree[i*2 + 1: i*2 + 3])

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

    def update(self, i, value):

        node = self.arr_len - 1 + i

        self.tree[node] = value

        while node > 0:
            node = (node - 1) // 2

            left_child = node * 2 + 1
            right_child = node * 2 + 2

            self.tree[node] = self.tree[left_child] + self.tree[right_child]

def solve():
    n,q = linput()
    l = linput()
    tree = SegmentTree(l)
    for x in range(q):
        t,l,r = linput()
        if t==2:
            print(tree.get_sum(l-1,r-1))
        else:
            tree.update(l-1,r)
        
            



for _ in range(1):
    solve()