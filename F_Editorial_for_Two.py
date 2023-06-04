for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    l = list(map(int,input().split()))
    l1 = sorted(l)
    c = 1
    mx = l1[k-1]
    for x in range(k-1,0,-1):
        if l1[x]==l1[x-1]:
            c+=1
        else:
            break
    
    a = []

    for x in range(1,n):
        if l[x]<mx:
            a.append(x)
        
        #this is a difficult problem was overenthu to try this thing 