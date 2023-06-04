for _ in range(int(input())):
    n=int(input())
    s = input()
    d = {}
    for x in range(1,n):
        d[s[x-1:x+1]] = 1
    print(len(d.values()))