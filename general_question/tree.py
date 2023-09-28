class Node:
    def __init__(self,data):
        self.l_tree=None
        self.r_tree=None 
        self.val=data

class Tree:
    def __init__(self):
        self.root=None

    def add(self,data):
        if(self.root == None):
            self.root = Node(data)
        else:
            self.add_node(data,self.root)

    def add_node(self,data,node):
        if(data < node.val):
            if(node.l_tree != None):
                self.add_node(data,node.l_tree)
            else:
                node.l_tree = Node(data)
        else:
            if(node.r_tree != None):
                self.add_node(data,node.r_tree)
            else:
                node.r_tree = Node(data)


    def printTree(self):
        if(self.root != None):
            self.print_tree(self.root)
        

    def print_tree(self,node):
        if(node!=None):
            self.print_tree(node.l_tree)
            print str(node.val) + ' '
            self.print_tree(node.r_tree)




tree=Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.print_tree(tree.root)
