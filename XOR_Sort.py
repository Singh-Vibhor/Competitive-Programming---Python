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
	mp = defaultdict(set)
	for x in range(n):
		mp[a[x]].add(x)
	temp = a[:]
	a.sort()
	ans = []
	for x in range(n):
		if x in mp[a[x]]:
			continue
		
		a1 = x
		a2 = mp[a[x]].pop()
		mp[temp[x]].remove(x)
		mp[temp[x]].add(a2)
		
		ans.append([a1+1,a2+1])
		ans.append([a2+1,a1+1])
		ans.append([a1+1,a2+1])
		
	print(ans)
		
		
		



for _ in range(int(input())):
    solve()