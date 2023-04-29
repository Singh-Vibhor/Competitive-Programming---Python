for _ in range(int(input())):
    n=int(input())
    s = bin(n)[2:]
    a1 = ""
    a2 = ""
    prv = 0
    f=1
    for x in s:
        if x=='1':
            if prv:
                f=0
                break
            else:
                prv = 1
                a1+='1'
                a2+='0'
        else:
            if prv:
                prv = 0
                a1+='1'
                a2+='1'
            else:
                a1+='0'
                a2+='0'
    if f and not prv:
        print(int(a1,2),int(a2,2))
    else:
        print(-1)
