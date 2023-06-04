from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    da = defaultdict(int)
    db = defaultdict(int)
    crra, crrb = 1, 1
    da[a[0]] = 1
    db[b[0]] = 1
    for x in range(1,n):
        if a[x]==a[x-1]:
            crra+=1
        else:
            crra = 1
        
        if b[x]==b[x-1]:
            crrb+=1
        else:
            crrb = 1

        da[a[x]] = max(da[a[x]],crra)
        db[b[x]] = max(db[b[x]],crrb)

    ans = 0
    for x in da.keys():
        ans = max(ans,da[x]+db[x])
    for x in db.keys():
        ans = max(ans,da[x]+db[x])
    print(ans)
