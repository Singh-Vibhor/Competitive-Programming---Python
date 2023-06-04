for _ in range(int(input())):
    s=input()
    f=1
    for x in range(1,len(s)):
        if s[x]!=s[x-1]:
            f=0
            break
    if f:
        print(-1)
    else:
        print(len(s)-1)