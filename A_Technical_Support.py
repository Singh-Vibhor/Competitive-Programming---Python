for _ in range(int(input())):
    n=int(input())
    s=input()
    ct=0
    for x in s:
        if x=='Q' and ct<0:
            ct=0
        if x=='Q':
            ct+=1
        else:
            ct-=1
    
    if s[0]=='A':
        print("No")
    elif ct<=0:
        print("Yes")
    else:
        print("No")