# IMSS
# I AM SAD SCAM

from collections import *
from sys import *
from heapq import *

input = stdin.readline 

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))

def convertBits(l):
    for x in range(len(l)):
        l[x] = [*bin(l[x]).replace('0b', '')]
        l[x] = ['0']*(32-len(l[x]))+l[x]
        l[x] = l[x][::-1]

MOD = 10**9+7


def solve():
    n,b,w,x = linput()
    prob = pow(6,-1,MOD)
    x = 100-x
    # print(prob)
    dp = [[[[[0, 0]for _ in range(x+1)] for _ in range(11)] for _ in range(b+1)] for _ in range(n+1)]
    dp[n][b][w][x][1] = 1
    
    for i in range(n,0,-1):
        for j in range(b,0,-1):
            for k in range(w,10):
                for l in range(x,-1,-1):

                    if((j-1)%6!=0):

                        dp[i-1][j-1][k][max(0,l-1)][0] += dp[i][j][k][l][1]*prob;
                        dp[i-1][j-1][k][max(0,l-1)][0] %= MOD;

                        dp[max(0,i-2)][j-1][k][max(0,l)][0] += dp[i][j][k][l][0]*prob;
                        dp[max(0,i-2)][j-1][k][max(0,l)][0] %= MOD;

                        dp[max(0,i-3)][j-1][k][max(0,l-3)][0] += dp[i][j][k][l][1]*prob;
                        dp[max(0,i-3)][j-1][k][max(0,l-3)][0] %= MOD;

                        dp[max(0,i-4)][j-1][k][max(0,l)][0] += dp[i][j][k][l][0]*prob;
                        dp[max(0,i-4)][j-1][k][max(0,l)][0] %= MOD;

                        dp[max(0,i-6)][j-1][k][max(0,l)][0] += dp[i][j][k][l][0]*prob;
                        dp[max(0,i-6)][j-1][k][max(0,l)][0] %= MOD;

                        if 1:
                            dp[max(0,i)][j-1][k+1][max(0,l)][0] += dp[i][j][k][l][0]*prob;
                            dp[max(0,i)][j-1][k+1][max(0,l)][0] %= MOD;

                        dp[i-1][j-1][k][max(0,l)][1] += dp[i][j][k][l][0]*prob;
                        dp[i-1][j-1][k][max(0,l)][1] %= MOD;

                        dp[max(0,i-2)][j-1][k][max(0,l-2)][1] += dp[i][j][k][l][1]*prob;
                        dp[max(0,i-2)][j-1][k][max(0,l-2)][1] %= MOD;

                        dp[max(0,i-3)][j-1][k][max(0,l)][1] += dp[i][j][k][l][0]*prob;
                        dp[max(0,i-3)][j-1][k][max(0,l)][1] %= MOD;

                        dp[max(0,i-4)][j-1][k][max(0,l-4)][1] += dp[i][j][k][l][1]*prob;
                        dp[max(0,i-4)][j-1][k][max(0,l-4)][1] %= MOD;

                        dp[max(0,i-6)][j-1][k][max(0,l-6)][1] += dp[i][j][k][l][1]*prob;
                        dp[max(0,i-6)][j-1][k][max(0,l-6)][1] %= MOD;
                    

                    else:

                        dp[i-1][j-1][k][max(0,l)][0] += dp[i][j][k][l][0]*prob;
                        dp[i-1][j-1][k][max(0,l)][0] %= MOD;
                        # print(i-1,j-1,k,l-1,dp[i-1][j-1][k][max(0,l-1)],dp[i][j][k][l][0])

                        dp[max(0,i-2)][j-1][k][max(0,l-2)][0] += dp[i][j][k][l][1]*prob;
                        dp[max(0,i-2)][j-1][k][max(0,l-2)][0] %= MOD;

                        dp[max(0,i-3)][j-1][k][max(0,l)][0] += dp[i][j][k][l][0]*prob;
                        dp[max(0,i-3)][j-1][k][max(0,l)][0] %= MOD;

                        dp[max(0,i-4)][j-1][k][max(0,l-4)][0] += dp[i][j][k][l][1]*prob;
                        dp[max(0,i-4)][j-1][k][max(0,l-4)][0] %= MOD;

                        dp[max(0,i-6)][j-1][k][max(0,l-6)][0] += dp[i][j][k][l][1]*prob;
                        dp[max(0,i-6)][j-1][k][max(0,l-6)][0] %= MOD;

                        if 1:
                            dp[max(0,i)][j-1][k+1][max(0,l)][1] += dp[i][j][k][l][0]*prob;
                            dp[max(0,i)][j-1][k+1][max(0,l)][1] %= MOD;

                        # print(i-1,j-1,k,l-1,dp[i-1][j-1][k][max(0,l-1)],dp[i][j][k][l][1],'1')
                        dp[i-1][j-1][k][max(0,l-1)][1] += dp[i][j][k][l][1]*prob;
                        dp[i-1][j-1][k][max(0,l-1)][1] %= MOD;
                        # print(i-1,j-1,k,l-1,dp[i-1][j-1][k][max(0,l-1)],dp[i][j][k][l][1], '1')

                        dp[max(0,i-2)][j-1][k][max(0,l)][1] += dp[i][j][k][l][0]*prob;
                        dp[max(0,i-2)][j-1][k][max(0,l)][1] %= MOD;

                        dp[max(0,i-3)][j-1][k][max(0,l-3)][1] += dp[i][j][k][l][1]*prob;
                        dp[max(0,i-3)][j-1][k][max(0,l-3)][1] %= MOD;

                        dp[max(0,i-4)][j-1][k][max(0,l)][1] += dp[i][j][k][l][0]*prob;
                        dp[max(0,i-4)][j-1][k][max(0,l)][1] %= MOD;

                        dp[max(0,i-6)][j-1][k][max(0,l)][1] += dp[i][j][k][l][0]*prob;
                        dp[max(0,i-6)][j-1][k][max(0,l)][1] %= MOD;

    ans = 0
    for i in range(b,-1,-1):
        for j in range(10):
            ans += dp[0][i][j][0][0] + dp[0][i][j][0][1]
            ans %= MOD
    # print(dp)
    # print(dp[n][b][w][x][1])
    # for i in range(n,0,-1):
    #     for j in range(b,0,-1):
    #         for k in range(w,-1,-1):
    #             for l in range(x,-1,-1):
    #                 ans += dp[i][j][k][l][0] + dp[i][j][k][l][1]
    #                 ans %= MOD
    print(ans)
    # print(dp[1][1][1][1][1], dp[0][0][1][0][1])
    # print((prob*prob*3)%MOD)
    # print(dp[0][4][2][0][1])


for _ in range(int(input())):
    solve()