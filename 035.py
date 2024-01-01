def throw(receiver, seconds):
    crr = receiver[0]
    vis = [-1]*(len(receiver))
    vis[0] = 0
    cnt = 1
    while vis[crr-1]==-1:
        vis[crr-1] = cnt
        crr = receiver[crr-1]
        cnt+=1
    mod = cnt - vis[crr-1]
    if seconds>=vis[crr-1]:
        seconds -= vis[crr-1]
        seconds %= mod
    
    st = 1
    while seconds>0:
        st = receiver[st-1]
        seconds -= 1
    
    return st
    

l = list(map(int,input().split()))
s = int(input())
print(throw(l,s))