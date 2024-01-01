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
	n = int(input())
	a = linput()
	b = linput()
	a.sort()
	b.sort()
	mx = 0
	mp = defaultdict(int)
	for x in range(n):
		mp[a[x]]+=1
		if a[x]>b[x]:
			print("NO")
			return
		
	for x in mp.values():
		if x > (n+1)//2:
			print("NO")
			return
	print("YES")



for _ in range(int(input())):
    solve()