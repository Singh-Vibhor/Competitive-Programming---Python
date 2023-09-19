import sys

input = sys.stdin.readline
def print(*args, end='\n', sep=' ') -> None:
    sys.stdout.write(sep.join(map(str, args)) + end)
def map_int():
    return map(int, input().split())
def list_int():
    return list(map(int, input().split()))
from collections import defaultdict




t = int(input())
for _ in range(t):
    n = int(input())
    arr = list_int()
    cur = 0
    starting = 0
    past_round = 0
    round = 0
    mn = 0
    for i, v in enumerate(arr):
        # print(i)
        cur += v
        if cur < mn:
            mn = cur
            if past_round<round:
                past_round = round
                starting = i


        if cur > 0:
            cur = 0
            round += 1

    pref = [0 for i in range(n+1)]
    for i in range(1, n+1):
        pref[i] = pref[i-1] + arr[i-1]
    # print(pref, starting)
    print(pref[starting])

