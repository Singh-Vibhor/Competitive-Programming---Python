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
    # n,g = linput()
    # a = linput()
    # b = linput()
    # mp = defaultdict(list)
    # for x in range(n):
    #     mp[a[x]].append(x)
    
    # a1 = sorted(a)
    # mapping = {}
    # for y,x in enumerate(a1):
    #     mapping[mp[x][0]] = y
    #     mp[x].pop(0)
    # # print(mapping)
    # b1 = sorted(b)
    # c1 = 0
    # for x in range(n):
    #     if a1[x]>b1[x]:
    #         c1+=1
    # p1 = n-1
    # p2 = n-1
    # crr = 0
    # ans1 = {}
    # while p2>=0:
    #     if a1[p1]>b1[p2]:
    #         crr+=1
    #         ans1[p2] = 1
    #         p1-=1
    #     p2-=1

    # p1 = n-1
    # p2 = n-1
    # crr1 = 0
    # while p2>=0:
    #     if b1[p1]>=a1[p2]:
    #         crr1+=1
    #         p1-=1
    #     p2-=1
    # if g >= (n-crr1) and g<=crr:
    #     print("YES")
    #     ans = []
    #     # print(ans1)
    #     for x in range(n):
    #         if x not in ans1:
    #             ans.append(b1[x])

    #     for x in range(n):
    #         if x in ans1:
    #             ans.append(b1[x])
    #     # print(ans)
    #     shift = crr - g
    #     shift = n-shift
    #     ans = ans[shift:] + ans[:shift]
    #     answer = [0]*n
    #     for x in range(n):
    #         answer[x] = ans[mapping[x]]
    #     # printl(a1)
    #     # printl(ans)
    #     # print(a, g)
    #     printl(answer)

    # else:
    #     print("NO")
    n,g = linput()
    g1 = g
    a = linput()
    b = linput()
    a1 = []
    for x,y in enumerate(a):
        a1.append([y,x])

    b.sort()
    a1.sort()
    # print(a1)
    ans = [0]*n

    for x in range(n):
        ans[a1[(n+x-g)%n][1]] = b[x]
    
    ch = 0
    for x in range(n):
        if a[x]>ans[x]:
            ch+=1
    if ch==g1:
        print("YES")
        printl(ans)
        return
    print("NO")





for _ in range(int(input())):
    solve()