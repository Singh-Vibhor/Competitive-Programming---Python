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

    def get_max(self, l, r):
        l += self.arr_len - 1
        r += self.arr_len - 1

        mx = 0

        while (l <= r):

            if ((l % 2) == 0):
                mx = max(mx,self.tree[l])

                l = (l + 1 - 1) // 2
            else:
                l = (l - 1) // 2

            if ((r % 2) == 1):
                mx = max(mx,self.tree[r])

                r = (r - 1 - 2) // 2
            else:
                r = (r - 2) // 2

        return mx

    def update(self, i, value):

        node = self.arr_len - 1 + i

        self.tree[node] = value

        while node > 0:
            node = (node - 1) // 2

            left_child = node * 2 + 1
            right_child = node * 2 + 2

            self.tree[node] = self.tree[left_child] + self.tree[right_child]




#remember binary search
#bitwise operator -> bitmask
def solve():
    n = int(input())
    a = linput()
    b = linput()
    
    



for _ in range(int(input())):
    solve()