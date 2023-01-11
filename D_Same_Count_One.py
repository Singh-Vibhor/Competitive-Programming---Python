import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    l=[]
    ct=[]
    for x in range(n):
        a=list(map(int,input().split()))
        l.append(a)
        cnt=0
        for y in a:
            if y==1:
                cnt+=1
        ct.append(cnt)

    oct=sum(ct)
    if oct%n!=0:
        print(-1)
    else:
        oct=int(oct/n)
        inc=dict()
        drc=dict()
        for i in range(n):
            if ct[i]>oct:
                inc[i]=ct[i]-oct
            elif ct[i]<oct:
                drc[i]=oct-ct[i]
        
        x=list(inc.keys())
        y=list(drc.keys())

        #print(inc,drc,x,y)
        x1=0
        y1=0
        print(sum(list(inc.values())))

        while x1<len(x) and y1<len(y):
            for j in range(m):
                if l[x[x1]][j]==1 and l[y[y1]][j]==0:
                    print(x[x1]+1,y[y1]+1,j+1)
                    l[x[x1]][j]=0
                    l[y[y1]][j]=1
                    f=0
                    inc[x[x1]]-=1
                    drc[y[y1]]-=1
                    if inc[x[x1]]==0:
                        x1+=1
                        f=1
                    if drc[y[y1]]==0:
                        y1+=1
                        f=1
                    if f:
                        break
            if x1==len(x) or y1==len(y):
                break