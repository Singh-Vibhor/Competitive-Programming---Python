for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    l = list(map(int,input().split()))
    l.sort()
    l1 = l[0]
    l2 = l[1]
    h1 = l[-1]
    h2 = l[-2]
    ans1 = (h1-l2)*min(n-1,m-1) + (h1-l1)*(n*m - min(n-1,m-1)-1)
    ans2 = (h2-l1)*min(n-1,m-1) + (h1-l1)*(n*m - min(n-1,m-1)-1)
    print(max(ans1,ans2))