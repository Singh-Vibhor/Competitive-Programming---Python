from collections import defaultdict
d=defaultdict(list)
for _ in range(int(input())-1):
    a, b = list(map(int,input().split()))
    d[a].append(b)
    d[b].append(a)

f=1
for x in d.values():
    if len(x)==2:
        f=0
        break
if f:
    print("YES")
else:
    print("NO")