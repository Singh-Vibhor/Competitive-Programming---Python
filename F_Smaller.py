for _ in range(int(input())):
    n=int(input())
    f1=0
    f2=0
    cn1=0
    cn2=0
    for i in range(n):
        l=input().split()

        

        if l[0]=='1':
            c1=0
            for x in l[2]:
                if x=='a':
                    c1+=1
                else:
                    f1=1
            cn1+=c1*int(l[1])
        else:
            c2=0
            for x in l[2]:
                if x=='a':
                    c2+=1
                else:
                    f2=1
            cn2+=c2*int(l[1])
    
        if f2:
            print("YES")
        elif f1:
            print("NO")
        elif cn1>=cn2:
            print("NO")
        else:
            print("YES")