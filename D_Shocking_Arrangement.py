for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c0 = 0
    neg = []
    pos = []
    for x in l:
        if x>0:
            pos.append(x)
        elif x<0:
            neg.append(x)
        else:
            c0+=1
    
    if c0==n:
        print("No")
    else:
        print("Yes")
        ans = []
        neg.sort()
        pos.sort(reverse = True)
        ng, ps, sm = 0, 0, 0
        while ng<len(neg) or ps<len(pos):
            if sm>0 and ng<len(neg):
                ans.append(neg[ng])
                sm+=neg[ng]
                ng+=1

            elif ps<len(pos):
                ans.append(pos[ps])
                sm+=pos[ps]
                ps+=1
            
        while c0>0:
            ans.append(0)
            c0-=1
        
        print(" ".join(map(str,ans)))
