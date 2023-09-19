l,h = list(map(int,input().split()))
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
f = 1
for x in range(l):
    if l1[x]+l2[x]>=h:
        print("NO")
        f = 0
        break
if f:
    print("YES")