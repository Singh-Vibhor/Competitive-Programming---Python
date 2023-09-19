# IMSS
# I AM SAD SCAM

from collections import *
from math import *
from sys import *
from heapq import *

def linput():
    return list(map(int,input().split()))

def printl(l):
    return print(' '.join(map(str,l)))



def solve():
    s=input()
    n=len(s)
    la,lb,lc,ld = [], [], [], []
    lfa, lfb, lfc, lfd = -1, -1, -1, -1
    sgn = [0]*(n*2)
    if "A" in s:
        lfa = s.index("A")
    if "B" in s:
        lfb = s.index("B")
    if "C" in s:
        lfc = s.index("C")
    if "D" in s:
        lfd = s.index("D")

    mp = {"A":1, "B":10, "C":100, "D":1000, "E":10000}
    ca,cb,cc,cd = 0, 0, 0, 0
    for x in s:
        if x=="A":
            ca+=1
        
        elif x=="B":
            cb+=1
            ca=0
        
        elif x=="C":
            cc+=1
            cb=0
            ca=0
        
        elif x=="D":
            cd+=1
            cc=0
            cb=0
            ca=0

        else:
            cd=0
            cc=0
            cb=0
            ca=0
        la.append(ca)
        lb.append(cb)
        lc.append(cc)
        ld.append(cd)
    
    fb = 0
    fc = 0
    fd = 0
    fe = 0
    change = {}
    ans = 0

    for x in range(n-1,-1,-1):
        y = s[x]

        if y=="A":
            if fc==0 and fd==0 and fe==0 and fb==0:
                ans+=mp["A"]
                sgn[x] = 0
            else:
                ans-=mp["A"]
                sgn[x] = 1

        if y=="B":
            if fc==0 and fd==0 and fe==0:
                ans+=mp["B"]
                sgn[x] = 0
            else:
                ans-=mp["B"]
                sgn[x] = 1
            if fc==0 and fd==0 and fe==0 and fb==0 and x!=0:
                if (la[x-1])*2+mp["A"]-mp["B"]>0:
                    change[(la[x-1])*2+mp["A"]-mp["B"]] = 1
            fb=1
        
        if y=="C":
            if fd==0 and fe==0:
                ans+=mp["C"]
                sgn[x] = 0
            else:
                ans-=mp["C"]
                sgn[x] = 1
            if fc==0 and fd==0 and fe==0 and x!=0:
                
                if ((la[x-1]*mp["A"] + lb[x-1]*mp["B"])*2 + mp["A"] - mp["C"])>0:
                    change[(la[x-1]*mp["A"] + lb[x-1]*mp["B"])*2 + mp["A"] - mp["C"]] = 1
                
                if lb[x-1]*mp["B"]*2 + mp["B"] - mp["C"]>0:
                    change[lb[x-1]*mp["B"]*2 + mp["B"] - mp["C"]] = 1
            fc = 1
                
        if y=="D":
            if fe==0:
                ans+=mp["D"]
                sgn[x] = 0
            else:
                ans-=mp["D"]
                sgn[x] = 1
            if fd==0 and fe==0 and x!=0:
                
                if ((la[x-1]*mp["A"] + lb[x-1]*mp["B"] + lc[x-1]*mp["C"])*2 + mp["A"] - mp["D"])>0:
                    change[(la[x-1]*mp["A"] + lb[x-1]*mp["B"] + lc[x-1]*mp["C"])*2 + mp["A"] - mp["D"]] = 1
                
                if (lb[x-1]*mp["B"] + lc[x-1]*mp["C"])*2 + mp["B"] - mp["D"]>0:
                    change[(lb[x-1]*mp["B"] + lc[x-1]*mp["C"])*2 + mp["B"] - mp["D"]] = 1

                if lc[x-1]*mp["C"]*2 + mp["C"] - mp["D"]>0:
                    change[lc[x-1]*mp["C"]*2 + mp["C"] - mp["D"]] = 1

            fd = 1
        
        if y=="E":
            ans+=mp["E"]
            sgn[x] = 0
            if fe==0 and x!=0:
                if ((la[x-1]*mp["A"] + lb[x-1]*mp["B"] + lc[x-1]*mp["C"] + ld[x-1]*mp["D"])*2 + mp["A"] - mp["E"])>0:
                    change[(la[x-1]*mp["A"] + lb[x-1]*mp["B"] + lc[x-1]*mp["C"] + ld[x-1]*mp["D"])*2 + mp["A"] - mp["E"]] = 1
                
                if (lb[x-1]*mp["B"] + lc[x-1]*mp["C"] + ld[x-1]*mp["D"])*2 + mp["B"] - mp["E"]>0:
                    change[(lb[x-1]*mp["B"] + lc[x-1]*mp["C"] + ld[x-1]*mp["D"])*2 + mp["B"] - mp["E"]] = 1

                if (lc[x-1]*mp["C"] + ld[x-1]*mp["D"])*2 + mp["C"] - mp["E"]>0:
                    change[(lc[x-1]*mp["C"] + ld[x-1]*mp["D"])*2 + mp["C"] - mp["E"]] = 1

                if ld[x-1]*mp["D"]*2 + mp["D"] - mp["E"]>0:
                    change[ld[x-1]*mp["D"]*2 + mp["D"] - mp["E"]] = 1
                
            fe = 1

    if lfa!=0 and lfa!=-1:
        if sgn[lfa]==0:
            change[mp["E"] - mp["A"] - 2*(ld[lfa-1]*mp["D"] + lc[lfa-1]*mp["C"] + lb[lfa-1]*mp["B"])] = 1
            change[mp["D"] - mp["A"] - 2*(lc[lfa-1]*mp["C"] + lb[lfa-1]*mp["B"])] = 1
            change[mp["C"] - mp["A"] - 2*(lb[lfa-1]*mp["B"])] = 1
            change[mp["B"] - mp["A"]] = 1
        else:
            change[mp["E"] + mp["A"] - 2*(ld[lfa-1]*mp["D"] + lc[lfa-1]*mp["C"] + lb[lfa-1]*mp["B"])] = 1
            change[mp["D"] + mp["A"] - 2*(lc[lfa-1]*mp["C"] + lb[lfa-1]*mp["B"])] = 1
            change[mp["C"] + mp["A"] - 2*(lb[lfa-1]*mp["B"])] = 1
            change[mp["B"] + mp["A"]] = 1
        
    
    if lfb!=0 and lfb!=-1:
        if sgn[lfb]==0:
            change[mp["E"] - mp["B"] - 2*(ld[lfb-1]*mp["D"] + lc[lfb-1]*mp["C"])] = 1
            change[mp["D"] - mp["B"] - 2*(lc[lfb-1]*mp["C"])] = 1
            change[mp["C"] - mp["B"]] = 1
        else:
            change[mp["E"] + mp["B"] - 2*(ld[lfb-1]*mp["D"] + lc[lfb-1]*mp["C"])] = 1
            change[mp["D"] + mp["B"] - 2*(lc[lfb-1]*mp["C"])] = 1
            change[mp["C"] + mp["B"]] = 1
    
    if lfc!=0 and lfc!=-1:
        if sgn[lfc]==0:
            change[mp["E"] - mp["C"] - 2*(ld[lfc-1]*mp["D"])] = 1
            change[mp["D"] - mp["C"]] = 1
        else:
            change[mp["E"] + mp["C"] - 2*(ld[lfc-1]*mp["D"])] = 1
            change[mp["D"] + mp["C"]] = 1
    
    if lfd!=0 and lfd!=-1:
        
        if sgn[lfd] == 0:
            change[mp["E"] - mp["D"]] = 1
        else:
            change[mp["E"] + mp["D"]] = 1

    
    if lfa==0:
        if sgn[lfa]==0:
            change[mp["E"]-mp["A"]] = 1
        else:
            change[mp["E"]+mp["A"]] = 1
    
    if lfb==0:
        if sgn[lfb]==0:
            change[mp["E"]-mp["B"]] = 1
        else:
            change[mp["E"]+mp["B"]] = 1

    if lfc==0:
        if sgn[lfc]==0:
            change[mp["E"]-mp["C"]] = 1
        else:
            change[mp["E"]+mp["C"]] = 1

    if lfd==0:
        if sgn[lfd]==0:
            change[mp["E"]-mp["D"]] = 1
        else:
            change[mp["E"]+mp["D"]] = 1
    
    l = list(change.keys())
    l.sort(reverse=True)
    #print(ans,l,ld)
    if len(l) and l[0]>0:
        ans+=l[0]
    print(ans)









for _ in range(int(input())):
    solve()