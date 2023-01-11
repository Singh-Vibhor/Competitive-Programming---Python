from collections import defaultdict as dd
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a1=[]
    a2=[]

    f=1

    l1=sorted(l)
    crr=0
    for x in l1:
        crr+=1
        if x<crr:
            f=0
            break
    
    d=dd(list)
    b1=[True]*(n+1)
    c1=1
    b2=[True]*(n+1)
    c2=1
    if f:
        for x in l1:
            if b1[x]:
                while not b2[c2]:
                    c2+=1
                    if c2==n+1:
                        break
                x1=x
                b1[x]=False
                x2=c2
                b2[c2]=False
                while not b2[c2]:
                    c2+=1
                    if c2==n+1:
                        break
                
            elif b2[x]:
                while not b1[c1]:
                    c1+=1
                    if c1==n+1:
                        break
                x2=x
                b2[x]=False
                x1=c1
                b1[c1]=False
                while not b1[c1]:
                    c1+=1
                    if c1==n+1:
                        break
            
            else:
                f=0
                break
            d[x].append([x1,x2])
    
    if f:
        print("YES")
        for x in l:
            
            a=d[x]
            
            a1.append(a[0][0])
            a2.append(a[0][1])
            if len(a)==2:
                a[0][0]=a[1][0]
                a[0][1]=a[1][1]
        print(" ".join(map(str,a1)))
        print(" ".join(map(str,a2)))
    
    else:
        print("NO")

                
