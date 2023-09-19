n,m,x,y = list(map(int,input().split()))
if n-x + 2*(m-y) > 25:
    print("LOLOS")
else:
    print("TIDAK LOLOS")