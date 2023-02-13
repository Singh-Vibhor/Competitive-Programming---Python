for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    l1=sorted(l)
    sm=0
    #0 1 2 3 4 5 6
    for x in range(n):
        sm+=l1[x]
        if sm>k:
            if x!=0:
                sm-=l1[x]+l1[x-1]
            sm+=l[x]
            #print(sm,"hi")
            break

    if sm<=k:
        print(n-x)
    else:
        print(n-x+1)


    
        

    #complete this later I am bored rn