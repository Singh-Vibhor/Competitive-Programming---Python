for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans = []
    for x in l:
        ans.append(n-x+1)
    print(" ".join(map(str,ans)))