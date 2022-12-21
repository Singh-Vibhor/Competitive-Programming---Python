for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l1=set(l)
    if len(l1)==1:
        print(0)
    
    elif len(l1)==2:
        a=min(l1)
        b=max(l1)
        cb=0
        for x in l:
            if x==b:
                cb+=1
        if cb>=2:
            print(2*b-a)
        else:
            print(b-2*a)
    
    else:
        l=list(l1)
        l.sort()
        a=len(l)
 
        ans1=2*l[a-1]-l[a-2]-l[a-3]
        ans2=2*l[2]-l[1]-l[0]
        ans3=l[2]+l[1]-2*l[0]
        ans4=0
        for x in range(2,a):
            z=2*l[x]-l[x-1]-l[0]
            if ans4<z:
                ans4=z
        ans5=0
        for x in range(2,a):
            z=l[x]-l[1]-2*l[0]
            if z>ans5:
                ans5=z
        ans6=max(l)-min(l)
        
        print(max(ans1,ans2,ans3,ans4,ans5,ans6))
