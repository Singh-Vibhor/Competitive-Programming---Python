for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    co = 0
    for x in l:
        if x%2: co+=1
    
    if co==0 or min(l)%2:
        print("YES")
    else:
        print("NO")