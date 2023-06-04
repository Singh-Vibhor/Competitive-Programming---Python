for _ in range(int(input())):
    n=int(input())
    s=input()
    stk = []
    f = 1
    ans = []
    for x in s:
        if len(stk)==0:
            stk.append(x)
            if x=='(':
                f = 1
            else:
                f = 2
        else:
            if stk[-1]==x:
                stk.append(x)
            else:
                stk.pop()
            
        ans.append(f)
    
    if len(stk)!=0:
        print(-1)
    else:
        if ans.count(1) and ans.count(2):
            print(2)
            print(" ".join(map(str,ans)))

        else:
            print(1)
            print(" ".join(['1']*len(s)))
                