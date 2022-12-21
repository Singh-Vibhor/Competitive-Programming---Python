for _ in range(int(input())):
    s=input()
    i=0
    x=0
    while (i+x)<len(s):
        if (i+x)<(len(s)-1):    
            if s[i+x]==s[i+x+1]:
                i=i+2
            elif s[i+x+1]==s[i+x+2]:
                i=i+2
                x=x+1
        else:
            x=x+1
             