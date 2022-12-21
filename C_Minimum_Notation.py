from collections import defaultdict as dd
for _ in range(int(input())):
    s=input()
    d=dd(int)
    d1=dd(int)
    high=0
    for x in s:
        x=int(x)
        if x>=high:
            d[x]+=1
            high=x
        
        else:
            d[x]+=1
            for y in range(9,x,-1):
                d1[min(y+1,9)]+=d[y]
                d[y]=0
                high=x
            
    l=[]
    for x in d.keys():
        l.extend([x]*d[x])
    
    for y in d1.keys():
        l.extend([y]*d1[y])
    
    l.sort()
    print("".join(list(map(str,l))))


