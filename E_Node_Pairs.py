def search(l,n):
    if n==1:
        return 2
    if n==2:
        return 2
    for x in range(2,n+1):
        if n==3:
            return 3
        if l[x]>n:
            return int(x-1)
        if l[x]==n:
            return int(x)


def prd(l):
    l.sort(reverse=True)
    #print(l)
    if len(l)==1 or len(l)==0:
        return 0
    crr=l[0]
    s=sum(l)
    #print(s)
    ans=crr*(s-crr)
    for x in range(1,len(l)):
        crr+=l[x]
        #print(ans)
        ans+=l[x]*(s-crr)
    return ans
        


n=int(input())
l=[0,1,1]
for x in range(2,n+3):
    l.append(l[x]+x)


ans=[]
while(n>0):
    x = search(l,n)
    #print(x)
    if x==1:
        ans.append(2)
    else:
        ans.append(x)
    n-=l[x]
    

print(sum(ans),prd(ans))

# dp for right solution



