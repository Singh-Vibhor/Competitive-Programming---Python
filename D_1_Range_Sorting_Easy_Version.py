from collections import defaultdict

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans = 0
    for i in range(n):
        # crr = 0
        arr = []
        # mp = defaultdict(int)
        # m1 = defaultdict(int)
        # dp = defaultdict(int)
        arr.append(l[i])
        # ln = 1
        # mp[l[i]] = i

        for j in range(i+1,n):
            if l[j]>arr[-1]:
                arr.append(l[j])
                # mp[l[j]] = j
                # ln+=1
                # dp[j] = dp[j-1]
                # m1[j] = j
                # ans+=dp[j]
                # print(l[j], dp[j],ans)
            
            else:
                # start = 0
                # end = ln
                # while start<end:
                #     mid = (start+end)//2
                #     if arr[mid]>l[j]:
                #         end = mid
                #     else:
                #         start = mid+1

                # prvcng = min(prvcng,mp[arr[start]])
                # crr = min(j - prvcng, crr+(j-mp[arr[start]]))
                # print(arr, l[j], j, crr, mp[arr[start]])
                
                # dp[j] = dp[mp[arr[start]]] + (j-mp[arr[start]])
                # print(arr, dp[j] , l[j], mp[arr[start]], dp[mp[arr[start]]], arr[start])
                # ans+=dp[j]

                crr = arr.pop()
                while len(arr) and l[j] < arr[-1]:
                    arr.pop()
                arr.append(crr)

            ans+=j-i+1-len(arr)
                
                


        
    print(ans)


