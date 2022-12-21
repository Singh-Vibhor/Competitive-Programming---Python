t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    f = 0
    for i in range(1, n):
        val = arr[i-1]+arr[i]
        val2 = arr[i-1]-arr[i]
        if val2>0 and arr[i]!=0 and arr[i-1]!=0:
            f = 1
            break 
        arr[i] = val
        

    if f:
        print(-1)
        continue
    
    for y in arr:
        print(y, end=" ")
    print("")