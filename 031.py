def mergesort(l):
    if len(l)==1: return l
    mid = len(l)//2

    a1 = l[:mid]
    a2 = l[mid:]
    a1 = mergesort(a1)
    a2 = mergesort(a2)

    p1,p2,p3 = 0, 0, 0

    while p1<len(a1) and p2<len(a2):
        if a1[p1]<a2[p2]:
            l[p3] = a1[p1]
            p1+=1
            p3+=1
        else:
            l[p3] = a2[p2]
            p3+=1
            p2+=1
        
    while p1<len(a1):
        l[p3] = a1[p1]
        p1+=1
        p3+=1

    while p2<len(a2):
        l[p3] = a2[p2]
        p3+=1
        p2+=1
    return l

a = list(map(int,input().split()))
print(" ".join(map(str,mergesort(a))))
    