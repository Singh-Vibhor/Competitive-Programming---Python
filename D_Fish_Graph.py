from collections import defaultdict
from types import GeneratorType
from functools import lru_cache
 
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    if not stack:
                        break
                    stack.pop()
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    graph = [[] for i in range(n+1)]
    for x in range(m):
        a, b = list(map(int,input().split()))
        graph[a].append(b)
        graph[b].append(a)
    cycles = [[] for i in range(n+1)]

    visited = defaultdict(int)
    

    def dfs_cycle(u, p, color: list, par: list):
        global cyclenumber
        if cyclenumber>=1:
            return

        if color[u] == 2:
            return
    
        if color[u] == 1:
            f = 0
            # v = []
            cur = p
            # v.append(cur)
            if len(graph[cur])>=4:
                f=1
                cycles[cyclenumber] = [cur]
                cyclenumber += 1
                return
            while cur != u:
                cur = par[cur]
                if len(graph[cur])>=4:
                    f=1
                    cycles[cyclenumber] = [cur]
                    cyclenumber += 1
                return
                # v.append(cur)
            if f:
                # cycles[cyclenumber] = v
                cyclenumber += 1
    
            return
    
        par[u] = p
    
        color[u] = 1
    
        for v in graph[u]:
    
            if v == par[u]:
                continue
            dfs_cycle(v, u, color, par)
    
        color[u] = 2

            
    color = [0] * (n+1)
    par = [0] * (n+1)
 
    cyclenumber = 0
 
    dfs_cycle(1, 0, color, par)

    f=1
    for x in cycles:
        if f==0: break
        d=[0]*(n+1)
        for y in x:
            if len(graph[y])>=4:
                # go for bfs with extra condition
                l=[(y,0)]
                vis = [0]*(n+1)
                vis[y] = 1
                par = [0]*(n+1)

                while len(l):
                    new = []
                    a1=-1
                    for x in l:
                        par[x[0]] = x[1]
                        if x[1]!=y and y in graph[x[0]]:
                            a1 = x[0]
                            break
                        for z in graph[x[0]]:
                            if not visited[z]:
                                new.append((z,x[0]))
                    l = new

                    
                    if a1!=-1:
                        break
                path = [a1]
                while a1!=y:
                    a1 = par[a1]
                    path.append(a1)
                # path.append(y)
                f = 0
                ans = []
                for x in graph[y]:
                    if x not in path:
                        ans.append([x,y])
                    
                    if len(ans)==2:
                        break
                for x in range(len(path)-1):
                    ans.append([path[x],path[x+1]])
                ans.append([path[-1],path[0]])
                print("YES")
                print(len(ans))
                print("\n".join(map(lambda x: str(x[0])+" "+str(x[1]),ans)))
                

                break

        
    if f:
        print("NO")


    # N, M = map(int, input().split())
    # ed = [set() for _ in range(N)]
    # for _ in range(M) :
    #     u, v = map(lambda x: int(x)-1, input().split())
    #     ed[u].add(v)
    #     ed[v].add(u)
    # fo = False
    # for u in range(N) :
    #     ta = ed[u].copy()
    #     if len(ta) < 4 :
    #         continue
    #     while len(ta) >= 2 :
    #         st = ta.pop()
    #         ex = [False for _ in range(N)]
    #         ex[u] = True
    #         ex[st] = True
    #         pi = [st]
    #         pr = [-1 for _ in range(N)]
    #         pr[st] = u
    #         while pi :
    #             cn = pi.pop()
    #             for nn in ed[cn] :
    #                 if ex[nn] : continue
    #                 pr[nn] = cn
    #                 if nn in ta :
    #                     end = nn
    #                     fo = True
    #                     break
    #                 ex[nn] = True
    #                 pi.append(nn)
    #             if fo : break
    #         if fo : break
    #     if fo : break
    # if not fo :
    #     print("NO")
    #     continue
    # print("YES")
    # ta = ed[u].difference({st, end})
    # fe = [(ta.pop(), u), (ta.pop(), u), (u, st), (end, u)]
    # cn = end
    # pn = pr[end]
    # while pn != u :
    #     fe.append((cn, pn))
    #     cn = pn
    #     pn = pr[cn]
    # print(len(fe))
    # for edge in fe :
    #     u, v = edge
    #     print(u+1, v+1)

        
