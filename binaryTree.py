class Node:
    def __init__(self, data = None,left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
class BinTree:
    def __init__(self):
        self.head = None
    def print(self):
        if self.head == None:
            print(None)
            return
        print(self.print1(self.head))
    def print1(self, top):
        if top == None:
            return
        return(f'{top.data} ({self.print1(top.left)}, {self.print1(top.right)})')
    def add_node(self, data):
        if self.head == None:
            self.head = Node(data, None, None)
            return
        self.add_node1(self.head, data)
    def add_node1(self, top, data):
        if data > top.data:
            if top.right:
                self.add_node1(top.right, data)
                return
            top.right = Node(data,None,None)
        else:
            if top.left:
                self.add_node1(top.left, data)
                return
            top.left = Node(data,None,None)

my_tree = BinTree()
my_tree.add_node(6)
my_tree.print()
my_tree.add_node(5)
my_tree.print()
my_tree.add_node(7)
my_tree.print()

my_tree.add_node(2)
my_tree.add_node(3)
my_tree.add_node(4)
my_tree.print()
