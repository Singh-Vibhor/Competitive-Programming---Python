m=998244353 
l=[1]
for x in range(40):
    l.append(((x+1)*l[x]))

for _ in range(int(input())):
    n=int(input())
    s=input()
    c0=0
    c1=0
    ans=0
    for x in range(n):
        if s[x]=='1':
            c1+=1
            for y in range(x-c1,x+1):
                ans+=int(l[x]/(l[y]*l[x-y]))
                ans%=m
        else:
            c0+=1
            for y in range(x-c0,x+1):
                ans+=int(l[x]/(l[y]*l[x-y]))
                ans%=m
    print(ans)

    #the logic was just a bit scam
    #TLE
