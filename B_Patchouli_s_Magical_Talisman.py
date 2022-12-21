import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    flag=True
    for x in a:
        if x%2==1:
            flag=False
            break
    mx=32
    nod=0
    
    for x in a:
        if x%2==1:
            nod+=1
        elif flag:
            while math.ceil(x/math.pow(2,mx))!=math.floor(x/math.pow(2,mx)):
                mx-=1
        
    if flag==False:
        print(n-nod)
    else:
        #print(mx)
        print(mx+n-1)

        
    
