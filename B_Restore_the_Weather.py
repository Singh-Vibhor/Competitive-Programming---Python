from collections import defaultdict
for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    l2.sort()
    mp = defaultdict(int)
    l3 = sorted(l1)
    for x in range(n):
        mp[l3[x]] = x

    ans = [0]*n
    for x in range(n):
        ans[mp[l3[x]]] = l2[x]
        mp[l3[x]]-=1
    
    print(" ".join(map(str,ans)))
