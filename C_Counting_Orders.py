m=10**9+7
for _ in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l1.sort(reverse = True)
    l2.sort(reverse = True)
    ans = 1
    f=1

    for x in range(n):
        if l2[x]>=l1[x]:
            print(0)
            f=0
            break

    if f:
        p1, p2 = 0, 0
        while True:
            while p1<n and l1[p1]>l2[p2]:
                p1+=1
            #print(p1,p2)
            ans *= p1-p2
            ans %= m
            p2+=1
            if p2>=n-1:
                break
        print(ans)
        