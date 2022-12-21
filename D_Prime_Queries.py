import math
l=[0,0,0,1]
l1=[2,3]
n=2
r=1
for x in range(4,100001):
    f=0
    a=math.sqrt(x)
    for y in l1:
        if x%y==0:
            f=1
            break
        if y>a:
            break

    if f==0:
        n+=1
        l1.append(x)
    
    if n%2==0:
        r+=1
    
    l.append(r)


for _ in range(int(input())):
    a,r=list(map(int,input().split()))
    print(l[r]-l[a-1])
