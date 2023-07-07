class Node:
    """
        We have common create new Node in below class's every method so,
        we will create class instead for this.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        # create new Node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self,value):
        # create new Node
        # add Node to end
        pass
    def prepend(self,value):
        pass
        # create new Node and add Node to beggining

    def insert(self,index,value):
        pass
        # create new Node and insert Node 

my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
        