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

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
