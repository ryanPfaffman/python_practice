class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        count = 0
        current = self.head
        while current.next != None:
            count += 1
            current = current.next
        return count

    def display(self):
        elems = []
        current = self.head
        while current.next != None:
            current = current.next
            elems.append(current.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print('Index out of Range')
            return None
        else:
            elems = []
            current = self.head
            while current.next != None:
                current = current.next
                elems.append(current.data)
            return elems[index]

    def erase(self, index):
        if index >= self.length():
            print('Index out of Range')
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

my_list = Linked_List()
my_list.append(1)
my_list.append(5)
my_list.append(10)
my_list.append(13)
print(my_list.length())
my_list.display()

my_list.erase(2)
my_list.display()
