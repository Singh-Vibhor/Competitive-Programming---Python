for _ in range(int(input())):
    x1,y1=list(map(int,input().split()))
    x2,y2=list(map(int,input().split()))
    x3,y3=list(map(int,input().split()))
    n=0
    if y1==y2 and y1!=0 and abs(y3)<abs(y2):
        n=abs(x2-x1)

    elif y2==y3 and y2!=0 and abs(y1)<abs(y2):
        n=abs(x3-x2)

    elif y3==y1 and y1!=0 and abs(y2)<abs(y3):
        n=abs(x3-x1)

    print(n)