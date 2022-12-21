from logging import root
from multiprocessing.pool import IMapUnorderedIterator


class TreeNode:
    def __init__(self, data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self, child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p = self.parent
        
        while p:
            level+=1
            p=p.parent
        
        return level

    def print_tree(self):

        spaces=' ' * self.get_level() * 2
        print(spaces + str(self.data))
        
        if self.children:
            for child in self.children:
                child.print_tree()
 
    
        

    

        

if __name__ == "__main__":
    #something here
    root=TreeNode(10)
    root.data=10
    a1=TreeNode(1)
    a2=TreeNode(2)
    a3=TreeNode(0)
    b1=TreeNode(0)
    b2=TreeNode(0)
    b3=TreeNode(0)
    c1=TreeNode(0)
    c2=TreeNode(0)
    d1=TreeNode(0)
    a1.data=1
    a2.data=2
    a3.data=3
    b1.data=4
    b2.data=5
    b3.data=6
    c1.data=7
    c2.data=8
    d1.data=9
    root.add_child(a1)
    root.add_child(a2)
    root.add_child(a3)
    a1.add_child(b1)
    a1.add_child(b2)
    a1.add_child(b3)
    a2.add_child(c1)
    a2.add_child(c2)
    a3.add_child(d1)

    root.print_tree()




