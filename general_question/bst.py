class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data

class Tree:
    def __init__(self):
        self.root = None

    def add(self,data):
        if(self.root == None):
            self.root = Node(data)
        else:
            self.add_n(data,self.root)

    def add_n(self,data,node):
        if(data < node.val):
            if(node.left != None):
                self.add_n(data,node.left)
            else:
                node.left = Node(data)
        else:
            if(node.right != None):
                self.add_n(data,node.right)
            else:
                node.right = Node(data)

    def find(self,data):
        if(self.root != None):
            return self.find_n(data,self.root)
        else:
            return None

    def find_n(self,data,node):
        if(data == node.val):
            return node
        elif(data < node.val and node.left != None):
            self.find_n(data,node.left)
        elif(data > node.val and node.right != None):
            self.find_n(data, node.right)

    def printTree(self):
        if(self.root != None):
            self.printTree_(self.root)

    def printTree_(self, node):
        if(node != None):
            self.printTree_(node.left)
            print str(node.val) + ' '
            self.printTree_(node.right)

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print (tree.find(8))
print tree.find(10)
tree.printTree()
