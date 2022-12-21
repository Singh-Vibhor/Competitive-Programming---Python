for _ in range(int(input())):
    ln=int(input())
    pos=list(map(int,input().split()))
    vel=list(map(int,input().split()))

    d=dict()

    t=[0]*len(pos)
    for x in range(len(pos)):
        t[x]=(ln-pos[x])/vel[x]
    
    for x in range(len(pos)):
        d[pos[x]]=t[x]
    
    pos.sort()

    high=0
    cnt=0
    for x in range(len(pos)-1,-1,-1):
        if d[pos[x]]>high:
            high=d[pos[x]]
            cnt+=1
            
    print(cnt)
