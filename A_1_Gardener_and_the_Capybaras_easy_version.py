for _ in range(int(input())):
    s=input()
    s1, s2, s3="", "", ""
    f=1
    for x in range(len(s)):
        if s[x]=='a' and x!=0 and x!=len(s)-1:
            s1=s[:x]
            s2=s[x]
            s3=s[x+1:]
            f=0
            break
    
    if f:
        s1=s[0]
        s2=s[1:len(s)-1]
        s3=s[len(s)-1]
    
    print(s1,s2,s3)
    
    