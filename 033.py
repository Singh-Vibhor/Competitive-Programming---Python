def countingSort(arr,mx):
    cnt = [0]*(mx+1)
    for x in arr:
        cnt[x]+=1
    for x in range(1,len(cnt)):
        cnt[x] += cnt[x-1]
    ans = [0]*(len(arr))
    for x in arr[::-1]:
        cnt[x]-=1
        ans[cnt[x]] = x
    return ans

l = list(map(int,input().split()))
print(" ".join(map(str,countingSort(l,max(l)))))
    
