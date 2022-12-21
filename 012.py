from calendar import IllegalMonthError


for _ in range(int(input())):
    n,m,r,c=list(map(int,input().split()))
    l=[]
    flag=False
    for x in range(n):
        s=input()
        if flag==False:
            if "B" in s:
                flag=True
        l.append(s)
    
    if flag:
        if l[r-1][c-1]=="B":
            print("0")
        elif "B" in l[r-1]:
            print("1")
        else:
            flag=True
            for x in l:
                if x[c-1]=="B":
                    flag=False
                    print("1")
                    break
            if flag:
                print("2")          


    else:
        print("-1")
