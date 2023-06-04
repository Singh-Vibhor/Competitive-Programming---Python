for _ in range(int(input())):
    n=int(input())
    s = input()
    ans = 2
    crr = 1
    for x in range(1,n):
        if s[x]==s[x-1]:
            crr+=1
        else:
            ans = max(ans,crr+1)
            crr = 1
    ans = max(ans,crr+1)
    print(ans)