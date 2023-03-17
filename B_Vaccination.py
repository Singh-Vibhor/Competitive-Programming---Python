for _ in range(int(input())):
    n,k,d,w = list(map(int,input().split()))
    l=list(map(int,input().split()))
    l.sort()
    ans = 0
    crr = l[0]
    cnt = 0
    for x in l:
        if cnt==k or x-crr>d+w:
            ans += 1
            crr = x
            cnt = 1
        else:
            cnt+=1
        
    print(ans+1)
            