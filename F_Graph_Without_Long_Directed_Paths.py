import sys
from collections import defaultdict
input = sys.stdin.readline
import queue

def possibleBipartition(n, dislikes):

    d=defaultdict(list)
    for x in dislikes:
        d[x[0]].append(x[1])
        d[x[1]].append(x[0])

    p=defaultdict(set)
    p[1].add(1)
    z=1
    que=queue.Queue()
    for x in d[1]:
        que.put(x)
    v=[True]*(n+1)
    v[1]=False
    while True:
        if que.qsize() == 0:
            f1=0
            for x in range(1,n+1):
                if v[x]:
                    f1=1
                    que.put(x)
                    break
            if f1==0:
                break
        if z==1:
            z=2
        else:
            z=1
        for x in range(que.qsize()):
            a = que.get()
            p[a].add(z)
            if v[a]:
                for x in d[a]:
                    que.put(x)
            v[a]=False

    '''f=True
    for x in p.values():
        if len(x)==2:
            f=False
            break'''
    return p

n,m=list(map(int,input().split()))
l=[]
for x in range(m):
    l.append(list(map(int,input().split())))

p = possibleBipartition(n,l)
f=1
for x in p.values():
    if len(x) == 2:
        f=0
        break

if f:
    ans=""
    for x in l:
        if list(p[x[0]])[0]==1:
            ans+="1"
        else:
            ans+="0"
    print("YES")
    print(ans)
else:
    print("NO") 
