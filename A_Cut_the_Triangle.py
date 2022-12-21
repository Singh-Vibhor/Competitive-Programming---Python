for _ in range(int(input())):
    s=input()
    x1,y1=list(map(int,input().split()))
    x2,y2=list(map(int,input().split()))
    x3,y3=list(map(int,input().split()))
    l1=[x1,x2,x3]
    l2=[y1,y2,y3]
    l1.sort()
    l2.sort()
    if (l1[0]==l1[1] or l1[1]==l1[2]) and (l2[0]==l2[1] or l2[1]==l2[2]):
        print("NO")
    else:
        print("YES")   