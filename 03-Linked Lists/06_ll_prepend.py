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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self,value):
        # create new Node
        # add Node to end
        new_node = Node(value)
        # if self.head is None:
        if self.length == 0:
            self.head = new_node
            # self.tail = new_node
        else:
            self.tail.next = new_node
            # self.tail = new_node
        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        # Pop return the last element from LL
        if self.length == 0:
            return None
        # Initially both pointing to head
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next 
        self.tail = pre 
        self.tail.next = None
        self.length -= 1
        # setting head & tail None
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self,value):
        """
            Pseudo Code:
                Prepend Method (value):
                    1. Create a new node with the given value.
                    2. If the list is empty,
                        a. Set the head and tail of the list to the new node.
                    3. Otherwise,
                        a. Connect the new node to the current head of the list.
                        b. Update the head of the list to the new node.
                    4. Increase the length of the list by 1.
                    5. Return True to indicate a successful operation.
        """
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True


my_linked_list = LinkedList(4)

my_linked_list.append(3)
my_linked_list.prepend(2)

print(my_linked_list.print_list())