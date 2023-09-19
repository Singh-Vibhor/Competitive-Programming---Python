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



def topologicalSort(graph,n):
         

    in_degree = [0]*(n)
        
    for i in graph:
        for j in graph[i]:
            in_degree[j] += 1


    queue = []
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    top_order = []

    while queue:

        u = queue.pop(0)
        top_order.append(u)
        for i in graph[u]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)
    return top_order


def solve():
    n,m,k = linput()
    h = linput()
    graph = defaultdict(list)
    for x in range(m):
        a,b = linput()
        graph[a-1].append(b-1)
    
    order = topologicalSort(graph,n)

    vis = [0]*n
    for x in order:
        if vis[x]:
            continue
        st = [x]
        





for _ in range(int(input())):
    solve()