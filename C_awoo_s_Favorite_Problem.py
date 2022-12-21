for _ in range(int(input())):
    n=int(input())
    s=input()
    t=input()
    s1=sorted(s)
    t1=sorted(t)
    if s1!=t1:
        print("NO")
    elif s==t:
        print("YES")
    else:
        a=0
        c=0
        flag=True
        for  x in range(n):
            if s[x]==t[x] and s[x]=='b':
                continue
            else:
                if (a!=0 and t[x]=='c') or (c!=0 and s[x]=='a'):
                    flag=False
                    break
                if s[x]=='a' and t[x]=='b':
                    a+=1
                elif s[x]=='b' and t[x]=='c':
                    c+=1
                elif s[x]=='b' and t[x]=='a':
                    a-=1
                    if a<0:
                        flag=False
                        break
                elif s[x]=='c' and t[x]=='b':
                    c-=1
                    if c<0:
                        flag=False
                        break
                elif (s[x]=='a' and t[x]=='c') or (s[x]=='c' and t[x]=='a'):
                    flag=False
                    break
                
        if flag:
            print("YES")
        else:
            print("NO")

