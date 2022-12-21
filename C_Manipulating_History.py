from collections import defaultdict as dd
for _ in range(int(input())):
    n=int(input())
    
    l1=[]
    for x in range(2*n):
        l1.append(input())

    l1.append(input())
    
    l2=[0]*26
    for x in range(2*n+1):
        for y in range(len(l1[x])):
            l2[ord(l1[x][y])-97]+=1
    
    for x in range(26):
        #print(l2[x])
        if l2[x]%2==1:
            print(chr(97+x))
            break
    



