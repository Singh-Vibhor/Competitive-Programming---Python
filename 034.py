from collections import defaultdict
def bucketSort(arr):
    mp = defaultdict(list)
    for x in arr:
        mp[str(x)[0]].append(x)
    # print(mp)
    ans = []
    for x in sorted(mp.keys()):
        ans += list(sorted(mp[x]))
    return ans

l = list(map(int,input().split()))
print(bucketSort(l))