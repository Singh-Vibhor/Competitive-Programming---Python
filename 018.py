from collections import defaultdict
import math
def areconnected(a, b):
  d = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
  if d<=a[2]+b[2]:
    return True
  return False
  

for _ in range(int(input())):
  x,y = list(map(int,input().split()))
  n=int(input())
  l=[]
  for z in range(n):
    l.append(list(map(int,input().split())))
  
  d = defaultdict(list)
  for a in l:
    for b in l:
      if a!=b:
        if areconnected(a,b):
          d[tuple(a)].append(tuple(b))
    if a[0]<=a[2]:
      d[tuple(a)].append('e1')
      d['e1'].append(tuple(a))
    if a[1]<=a[2]:
      d[tuple(a)].append('e2')
      d['e2'].append(tuple(a))
    if a[0]+a[2]>=x:
      d[tuple(a)].append('e3')
      d['e3'].append(tuple(a))
    if a[1]+a[2]>=y:
      d[tuple(a)].append('e3')
      d['e3'].append(tuple(a))
  
  def dfs(start, find):
    d1 = defaultdict(bool)
    l=[start]
    while len(l):
      a = l.pop()
      if a == find:
        return True
      for x in d[a]:
        if x not in d1:
          d1[x] = True
          l.append(x)
        
    return False
  
  if dfs('e1','e3') or dfs('e2', 'e3'):
    print("NO")
  else:
    print("YES")


#solved successfully!
    
    
  