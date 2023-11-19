class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None
    
    def __find(self,node,parent,value):
        if node==None:
            return None,parent,False
        
        if value<node.data:
            if node.left: #sushestvuet
                return self.__find(node.left,node,value)
            
        if value>node.data:
            if node.right: #sushestvuet
                return self.__find(node.right,node,value)

        if value==node.data:
            return node, parent, True

        return node, parent, False

    def append(self,obj):
        if self.root==None:
            self.root=obj
            return obj
        else:
            s,p,fl_find=self.__find(self.root, None, obj.data)
            if not fl_find and s:
                if obj.data<s.data:
                    s.left=obj
                else:
                    s.right=obj
            return obj
        
    def __del_leaf(self, s, p):
        if p.left==s:
            p.left=None
        elif p.right==s:
            p.right=None
    

    def __del_one_child(self, s, p):
        if p.left==s:
            if s.left==None:
                p.left=s.right
            elif s.right==None:
                p.left=s.left

        elif p.right==s:
            if s.left==None:
                p.right=s.right
            elif s.right==None:
                p.right=s.left
    

    def __find_min(self,node, parent):
        if node.left:
            return self.__find_min(node.left,node)
        
        return node, parent

    def del_node(self,key):
        s,p,fl_find=self.__find(self.root, None, key)

        if not fl_find:
            return None
        if s.left==None and s.right==None: #1 Listovoy
            self.__del_leaf(s,p)

        elif s.left==None or s.right==None: #2 1 potomok
            self.__del_one_child(s,p)

        else:
            sr, pr=self.__find_min(s.right,s)
            s.data=sr.data
            self.__del_one_child(sr,pr)

    def show_tree(self,node):
        if node==None:
            return
        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def show_wide_tree(self,node):
        if node==None:
            return
        




v=[10,5,7,16,13,2,20,20]

t=Tree()

for x in v:
    t.append(Node(x))

t.show_tree(t.root)

t.del_node(5)

print("\nDONE\n")
t.show_tree(t.root)
