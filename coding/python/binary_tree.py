class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if self.val == data:
            return False
        elif self.val > data:
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return True

    def find(self, data):
        if self.val == data:
            return True
        elif self.val > data:
            if self.left_child:
                return self.left_child.find(data)
            else:
                return False
        else:
            if self.right_child:
                return self.right_child.find(data)
            else:
                return False

    def pre_order(self):
        if self:
            print(str(self.val))
            if self.left_child:
                self.left_child.pre_order()
            if self.right_child:
                self.right_child.pre_order()

    def post_order(self):
        if self:
            if self.left_child:
                self.left_child.post_order()
            if self.right_child:
                self.right_child.post_order()
            print(str(self.val))

    def in_order(self):
        if self:
            if self.left_child:
                self.left_child.in_order()
            print(str(self.val))
            if self.right_child:
                self.right_child.in_order()

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def pre_order(self):
        print("PreOrder")
        self.root.pre_order()

    def post_order(self):
        print("PostOrder")
        self.root.post_order()

    def in_order(self):
        print("InOrder")
        self.root.in_order()

bst = Tree()
bst.insert(1)
bst.insert(2)
bst.insert(5)
bst.insert(7)
bst.insert(17)
bst.insert(300)
bst.insert(22)
bst.insert(25)
bst.insert(243)
bst.insert(22)
bst.insert(10)
bst.insert(15)

print(bst.pre_order())
