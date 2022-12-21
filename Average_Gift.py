for _ in range(int(input())):
    n,x=list(map(int,input().split()))
    l=list(map(int,input().split()))
    l.sort()
    #I have to make 0 with any number that is a factor of n
    if x>=l[0] and x<=l[n-1]:
        print("YES")
    else:
        print("NO")
        
        