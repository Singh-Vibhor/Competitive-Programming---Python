for _ in range(int(input())):
    n=int(input())
    ans=[]
    if n%2:
        ans.append(int(n/2)+1)
        for x in range(1,int(n/2)+1):
            ans.append(x)
            ans.append(x+int(n/2)+1)
        
    else:
        for x in range(int(n/2),0,-1):
            ans.append(x)
            ans.append(x+int(n/2))
        
    print(" ".join(map(str,ans)))