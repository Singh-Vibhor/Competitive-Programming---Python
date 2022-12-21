n,d=list(map(int,input().split()))
l=list(map(int,input().split()))
l.sort()
a=-1
b=n-1
ans=0
crr=1
while(a<b):
    while crr*l[b]<=d and a<b:
        a+=1
        crr+=1
    if a<b:
        ans+=1
        b-=1
        crr=1
print(ans)
