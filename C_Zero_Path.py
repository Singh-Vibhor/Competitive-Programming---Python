for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    l=[]
    for x in range(n):
        l.append(list(map(int,input().split())))
    #print(l)
    if False:
        print("YES")
        

    
    else:
        
        dpmin = []
        dpmax = []
        mn = []
        mx = []
        for i in range (0, n):
            for j in range (0, m):
                mn.append(1000)
                mx.append(-1000)
            dpmin.append(mn)
            dpmax.append(mx)
            mn = []
            mx=[]

        
        dpmin[0][0]=l[0][0]
        dpmax[0][0]=l[0][0]

        for x in range(1,m):
            dpmin[0][x]=l[0][x]+dpmin[0][x-1]
            dpmax[0][x]=l[0][x]+dpmax[0][x-1]

        for x in range(1,n):
            dpmin[x][0]=l[x][0]+dpmin[x-1][0]
            dpmax[x][0]=l[x][0]+dpmax[x-1][0]

        for x in range(1,n):
            for y in range(1,m):
                dpmin[x][y]=min(dpmin[x-1][y],dpmin[x][y-1])+l[x][y]
                dpmax[x][y]=max(dpmax[x-1][y],dpmax[x][y-1])+l[x][y]

        
        if dpmax[n - 1][m - 1] % 2 == 1 or dpmin[n - 1][m - 1] > 0 or dpmax[n - 1][m - 1] < 0:
            print("NO")
        else:
            print("YES")