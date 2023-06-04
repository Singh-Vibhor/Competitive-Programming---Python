from collections import defaultdict

class TreeNode:

    def __init__(self, n) -> None:
        self.children = []
        self.val = n



for _ in range(int(input())):
    n=int(input())
    d = defaultdict(int)
    d[1] = 1

    tree = {}
    ans = 1

    for z in range(n-1):
        a,b = list(map(int,input().split()))

        # if a not in d:
        #     if a not in tree:
        #         a1 = TreeNode(a)
        #         tree[a] = a1
        #     if b not in tree:
        #         b1 = TreeNode(b)
        #         tree[b] = b1
        #     tree[a].children.append(tree[b])
        
        # else:
        if a in d and b in d:
            if d[a]==d[b]:
                continue
            if d[a]>d[b]:
                temp = a
                a = b
                b = temp
            d[b] = d[a]
            crr = d[a]+1
            if b in tree:
                b = tree[b]
                visited = {b.val:1}
                l = []
                for x in b.children:
                    l.append(x.val)
                    visited[x.val] = 1
                
                while len(l):
                    for x in range(len(l)):
                        c = l.pop(0)
                        visited[c] = 1
                        c = tree[c]
                        if c.val not in d:
                            d[c.val] = crr
                        d[c.val] = min(d[c.val],crr)
                        for x in c.children:
                            if x.val not in visited:
                                l.append(x.val)
                                visited[x.val] = 1
                        

                    crr+=1


        elif a in d:
            d[b] = d[a]
            crr = d[a]+1
            if b in tree:
                b = tree[b]
                visited = {b.val:1}
                l = []
                for x in b.children:
                    l.append(x.val)
                    visited[x.val] = 1
                
                while len(l):
                    for x in range(len(l)):
                        c = l.pop(0)
                        visited[c] = 1
                        c = tree[c]
                        if c.val not in d:
                            d[c.val] = crr
                        d[c.val] = min(d[c.val],crr)
                        for x in c.children:
                            if x.val not in visited:
                                l.append(x.val)
                                visited[x.val] = 1
                        

                    crr+=1
        
        elif b in d:
            d[a] = d[b]
            crr = d[b]+1
            b = a
            if b in tree:
                b = tree[b]
                visited = {b.val:1}
                l = []
                for x in b.children:
                    l.append(x.val)
                    visited[x.val] = 1
                
                while len(l):
                    for x in range(len(l)):
                        c = l.pop(0)
                        visited[c] = 1
                        c = tree[c]
                        if c.val not in d:
                            d[c.val] = crr
                        d[c.val] = min(d[c.val],crr)
                        for x in c.children:
                            if x.val not in visited:
                                l.append(x.val)
                                visited[x.val] = 1
                        

                    crr+=1
        
        if a not in d and b not in d:
            if a not in tree:
                tree[a] = TreeNode(a)
            if b not in tree:
                tree[b] = TreeNode(b)
            
            tree[a].children.append(tree[b])
            tree[b].children.append(tree[a])
        

    print(max(list(d.values())))

            