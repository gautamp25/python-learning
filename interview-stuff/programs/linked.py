class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_node(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        prev_node.next = curr_node.next
        curr_node = None
    
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

my_list = LinkedList()
my_list.append(1)
my_list.append(2)

my_list.append(3)
my_list.prepend(0)
my_list.print_list()
my_list.insert_after_node(my_list.head.next, 1.5)
my_list.delete_node(1)
my_list.print_list()  # Output: 0 2 1.5 3