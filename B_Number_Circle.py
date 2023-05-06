n = int(input())
l = list(map(int,input().split()))
l.sort()
if l[n-1]>=l[n-2]+l[n-3]:
    print("NO")
else:
    print("YES")
    temp = l[n-1]
    l[n-1] = l[n-2]
    l[n-2] = temp
    print(" ".join(map(str,l)))