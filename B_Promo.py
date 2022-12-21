n,q=list(map(int,input().split()))
b=list(map(int,input().split()))
b.sort(reverse=True)
#print(a)
for z in range(1,n):
    
    b[z]+=b[z-1]

for z in range(q):
    
    x,y=list(map(int,input().split()))
    y=x-y
    
    if y!=0:
        print(b[x-1]-b[y-1])
    
    
    else:
        print(b[x-1])
