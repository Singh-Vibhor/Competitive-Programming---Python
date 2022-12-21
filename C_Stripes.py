for _ in range(int(input())):
    a=input()
    ans='B'
    for x in range(8):
        a=input()
        f1=1
        for y in a:
            if y=="B" or y==".":
                f1=0
        if f1:
            ans='R'
    
    print(ans)
            