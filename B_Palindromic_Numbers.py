for _ in range(int(input())):
    n=int(input())
    s=input()
    l=[0]*n

    if s[0]!='9':
        if int(s[0])>=int(s[n-1]):
            l[0]=1
            l[n-1]=int(s[0])-int(s[n-1])+1
        else:
            l[0]=int(s[n-1])-int(s[0])
        for x in range(1,int(n/2)):
            if int(s[x])>int(s[n-x-1]):
                l[n-x-1]=int(s[x])-int(s[n-x-1])
            else:
                l[x]=int(s[n-x-1])-int(s[x])
        
        print(''.join(map(str,l)))
        
    else:
        a='1'+'2'*(n-1)+'1'
        ans=int(a)-int(s)
        print(ans)

        