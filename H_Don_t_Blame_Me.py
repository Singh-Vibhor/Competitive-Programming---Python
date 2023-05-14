m = 10**9+7
for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    l =list(map(int,input().split()))
    dp = [[0]*64 for x in range(n)]
    
    dp[0][l[0]]+=1
    for x in range(1,n):
        dp[x][l[x]]+=1
        for y in range(64):
            dp[x][y] += dp[x-1][y]
            dp[x][y] %= m
            dp[x][y & l[x]] += dp[x-1][y]
            dp[x][y & l[x]] %= m

    ans = 0
    for x in range(64):
        k1 = 0
        x1 = x
        while x>0:
            k1 += x%2
            x //= 2
        if k1 == k:
            ans += dp[n-1][x1]
            ans %= m
    print(ans%m)