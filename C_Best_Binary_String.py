for _ in range(int(input())):
    s=input()
    ans = [""]*len(s)
    if s[0]=='?':
        ans[0] = '0'
    else:
        ans[0] = s[0]
    
    for x in range(1,len(s)):
        if s[x]=='?':
            ans[x]=ans[x-1]
        else:
            ans[x]=s[x]
    
    print("".join(ans))